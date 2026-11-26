# SmartSpend: Multi-Agent Upgrade

SmartSpend can now be orchestrated as a supervisor with four focused specialist agents,
while reusing the existing deterministic Python finance tools.

- Expense Analyst
- Budget Agent
- Anomaly Investigator
- Savings & Planning Agent

See [architecture documentation](docs/architecture.md) and `agents/multi_agent.py`.

The implementation is additive and requires the existing notebook tools plus the notebook's
configured LLM. This new architecture layer is not yet validated against a running Ollama
server/model; run the notebook integration and runtime tests before deployment.
