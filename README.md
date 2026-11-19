# SmartSpend — AI Personal Finance Agent

SmartSpend is an agentic personal-finance assistant that turns bank-export CSV data into structured spending insights. It can parse and categorize transactions, summarize income and expenses, manage category budgets, flag unusual activity, and calculate a savings plan.

The agent is built with **LlamaIndex FunctionAgent** and **Qwen3 4B** served locally by **Ollama**. Financial calculations are performed by deterministic Python/Pandas tools; the language model is responsible for understanding requests and selecting tools.

> **Project status:** The notebook's Python tool layer and its validation tests have saved execution outputs. The live Qwen3/Ollama agent setup and conversation examples are included in the notebook but still need to be run in a Colab runtime with Ollama available. No agent conversation results are claimed as completed.

## Highlights

- CSV transaction ingestion and normalization
- Rule-based expense categorization
- Date-filtered financial summaries
- Category budget creation and budget-status analysis
- Possible duplicate and unusually large expense detection
- Savings targets and suggested discretionary reductions
- Tool-calling workflow with conversation context
- Safety instructions against invented financial data and money transfers

## Repository structure

```text
smartspend-ai-agent/
├── data/
│   └── transactions.csv          # Synthetic example bank export (42 rows)
├── notebooks/
│   └── SmartSpend_Agent.ipynb    # Main notebook with saved tool-test outputs
├── .gitignore
├── README.md
└── requirements.txt
```

## Architecture

```text
User request + transaction CSV
            |
            v
     Qwen3 4B via Ollama
            |
            v
   LlamaIndex FunctionAgent
            |
            v
       Seven Python tools
            |
   +--------+---------+-------------------+
   |        |         |                   |
   v        v         v                   v
 Parse   Categorize  Financial summary   Budget tools
                                         |
                              +----------+----------+
                              |                     |
                              v                     v
                       Anomaly detection      Savings plan
                              |
                              v
                    Tool results to the agent
                              |
                              v
                     Financial explanation
```

## The seven tools

| Tool | Responsibility |
|---|---|
| `parse_transactions` | Reads CSV text or a CSV file path and normalizes transaction records |
| `categorize_transactions` | Assigns expenses to supported spending categories |
| `calculate_financial_summary` | Calculates income, expenses, savings, and category distribution for a date range |
| `manage_budget` | Creates or updates category spending limits |
| `analyze_budget_status` | Compares category spending with budget limits |
| `detect_anomalies` | Flags possible duplicates and unusually large expenses |
| `calculate_savings_plan` | Calculates a savings target and possible expense reductions |

The tools use Pandas/Python for numeric calculations. The notebook also uses a small in-memory session state so later tool calls can reuse parsed transactions and saved budgets without repeatedly passing large transaction lists.

## Technology stack

- Python
- Pandas
- LlamaIndex Core
- LlamaIndex Ollama integration
- Ollama
- Qwen3 4B
- Google Colab (notebook environment)

## Quick start (Google Colab)

The notebook is designed to be run in Google Colab. A T4 GPU runtime is recommended where available.

1. Open [SmartSpend_Agent.ipynb](notebooks/SmartSpend_Agent.ipynb) in GitHub.
2. Download the notebook or open it in Google Colab.
3. In Colab, select **Runtime → Change runtime type → T4 GPU** (if available).
4. Run the notebook from the first cell, in order.
5. The setup cells install the Python packages, install/start Ollama, and pull `qwen3:4b`.
6. Continue through the agent setup and example conversation cells.

The notebook's sample data cell creates `data/transactions.csv`. A copy is also included in this repository for inspection and reuse.

### Local environment

Install the Python dependencies:

```bash
python -m venv .venv
```

Activate the environment:

```bash
# macOS / Linux
source .venv/bin/activate

# Windows PowerShell
.venv\Scripts\Activate.ps1
```

Install packages:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Install [Ollama](https://ollama.com/download), start its service, and download the model:

```bash
ollama pull qwen3:4b
```

Then open the notebook in Jupyter or Colab and run the cells in order. The notebook includes Colab-specific shell commands, so local execution may require adapting those setup cells for your operating system.

## Sample data and validated results

`data/transactions.csv` is **synthetic demonstration data**, not real bank information. It contains 42 transactions for October 2026, including deliberately repeated charges and large purchases to exercise the anomaly detector.

The saved Python-tool validation in the notebook reports the following results for this sample:

| Metric | Result |
|---|---:|
| Transactions | 42 |
| Total income | $4,850.00 |
| Total expenses | $4,361.39 |
| Remaining balance / savings | $488.61 |
| Savings rate | 10.1% |
| Possible anomalies flagged | 4 |

The sample budget test reports exceeded limits for Food, Entertainment, Healthcare, and Shopping. These values are examples from the included synthetic dataset, not financial advice or results for a real user.

## Safety, privacy, and limitations

- SmartSpend is an analysis and recommendation prototype. It does **not** initiate transfers, payments, or other financial transactions.
- An anomaly is only a signal for review; it is not proof of fraud.
- Never commit real bank statements, account numbers, credentials, or other private financial information.
- The included dataset is synthetic. Replace it only with data you are authorized to process, and keep personal data out of public repositories.
- Categorization is keyword-based; unfamiliar merchants may be classified as `Other`.
- Anomaly detection uses heuristic thresholds and can produce false positives or miss unusual activity.
- Session state is stored in memory and resets when the Python runtime restarts.
- A small local model may select an incorrect tool or provide an imperfect explanation. Verify important outputs.
- Ollama availability, model download size, GPU access, and Colab runtime limits can affect setup and performance.

## Validation status

- **Python tools:** executed in the notebook; assertions cover parsing, categorization, date filtering, budget handling, anomaly detection, savings calculations, and invalid-input handling.
- **Plain-Python pipeline:** executed against the sample CSV in the notebook.
- **Qwen3 agent integration:** setup and conversation examples are present, but their cells have no saved execution outputs yet. Run these cells in a working Ollama runtime before describing the full agent workflow as end-to-end validated.

## Future improvements

- Add a reusable Python package and automated test suite.
- Improve merchant categorization with configurable rules or a trained classifier.
- Add configurable anomaly thresholds and richer explanations.
- Add secure, local-only data ingestion and redaction options.
- Add reproducible agent evaluation for tool selection, numeric faithfulness, and refusal behavior.

## License

No license has been added yet. Until a license is selected, the repository should be treated as all-rights-reserved by default.
