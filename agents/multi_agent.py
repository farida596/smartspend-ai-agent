"""Composable SmartSpend multi-agent system built with LlamaIndex FunctionAgent.

This module reuses the project's existing deterministic finance tools. It does not
replace calculations with LLM-generated arithmetic.
"""
from __future__ import annotations

from typing import Any, Dict, Iterable, List

from llama_index.core.tools import FunctionTool
from llama_index.core.agent.workflow import FunctionAgent
from llama_index.core.workflow import Context

WORKER_TOOL_MAP = {
    "expense_analyst": ["parse_transactions", "categorize_transactions", "calculate_financial_summary"],
    "budget_agent": ["manage_budget", "analyze_budget_status"],
    "anomaly_investigator": ["detect_anomalies"],
    "savings_forecast_agent": ["calculate_savings_plan"],
}

WORKER_PROMPTS = {
    "expense_analyst": """You are SmartSpend's Expense Analyst. Analyze transaction data,
categorization, income, spending, date ranges and comparisons. Use tools for figures.
Explain patterns clearly and do not invent missing transaction data.""",
    "budget_agent": """You are SmartSpend's Budget Agent. Set or analyze category budgets,
budget utilization, remaining amounts and over-budget categories. Use tools for all figures.
Do not invent budgets or actual spend.""",
    "anomaly_investigator": """You are SmartSpend's Anomaly Investigator. Review transaction
flags and describe why an item merits review. An anomaly or duplicate flag is NOT proof
of fraud. Do not invent evidence.""",
    "savings_forecast_agent": """You are SmartSpend's Savings & Planning Agent. Use the
savings calculation tools to estimate targets and practical reductions. Clearly label
assumptions and avoid guaranteeing future outcomes.""",
}

SUPERVISOR_PROMPT = """You are SmartSpend's Supervisor, coordinating specialist agents
for personal-finance analysis.

Delegate to one or more specialists as needed:
- Expense Analyst: transaction summaries, categories, income/expense, period analysis.
- Budget Agent: budget setup, budget status, utilization, limit concerns.
- Anomaly Investigator: suspiciously unusual or duplicate-looking transactions.
- Savings & Planning Agent: savings targets and reductions.

For multi-part questions, delegate to every relevant specialist, then combine their results
into one coherent, concise answer. Use tool-derived numbers, not mental arithmetic.
If the data needed for a task is missing, say what is missing rather than fabricate.
Never claim anomaly flags prove fraud, and never execute transfers/payments.
Avoid unnecessary delegation for simple questions.
"""

def _as_text(output: Any) -> str:
    """Extract a stable textual representation from LlamaIndex agent outputs."""
    for attr in ("response", "output", "message"):
        value = getattr(output, attr, None)
        if value is not None:
            return str(value)
    return str(output)

def build_multi_agent_system(llm: Any, finance_tools: Iterable[Any]):
    """Build supervisor and four specialist agents from existing FunctionTools.

    Args:
        llm: LlamaIndex-compatible LLM (the notebook's Ollama instance works).
        finance_tools: Iterable of existing FunctionTool instances.

    Returns:
        dict with supervisor, workers, and fresh supervisor Context.
    """
    tools_by_name: Dict[str, Any] = {
        tool.metadata.name: tool for tool in finance_tools
    }
    missing = sorted({name for names in WORKER_TOOL_MAP.values() for name in names} - tools_by_name.keys())
    if missing:
        raise ValueError(f"Missing finance tools required for multi-agent setup: {missing}")

    workers: Dict[str, FunctionAgent] = {}
    worker_contexts: Dict[str, Context] = {}
    for worker_name, names in WORKER_TOOL_MAP.items():
        workers[worker_name] = FunctionAgent(
            name=worker_name,
            description=WORKER_PROMPTS[worker_name],
            tools=[tools_by_name[name] for name in names],
            llm=llm,
            system_prompt=WORKER_PROMPTS[worker_name],
        )
        worker_contexts[worker_name] = Context(workers[worker_name])

    # These async wrappers expose delegation as callable tools for the supervisor.
    delegation_tools: List[Any] = []
    def make_delegate(name: str):
        async def delegate(query: str) -> str:
            """Forward a question to the selected specialist and return its response."""
            result = await workers[name].run(query, ctx=worker_contexts[name])
            return _as_text(result)
        delegate.__name__ = f"ask_{name}"
        delegate.__doc__ = f"Delegate financial analysis to {name.replace('_', ' ')}. Provide the task/question."
        return delegate

    for worker_name in WORKER_TOOL_MAP:
        delegate = make_delegate(worker_name)
        delegation_tools.append(FunctionTool.from_defaults(fn=delegate, name=delegate.__name__, description=delegate.__doc__))

    supervisor = FunctionAgent(
        name="SmartSpendSupervisor",
        description="Coordinates specialist personal-finance agents.",
        tools=delegation_tools,
        llm=llm,
        system_prompt=SUPERVISOR_PROMPT,
    )
    return {
        "supervisor": supervisor,
        "supervisor_context": Context(supervisor),
        "workers": workers,
        "worker_contexts": worker_contexts,
    }
