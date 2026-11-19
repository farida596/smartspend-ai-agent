# SmartSpend – AI Personal Finance Agent

SmartSpend is an AI-powered personal finance agent designed to help users manage their money by analyzing financial transactions, categorizing expenses, monitoring budgets, detecting unusual spending, and creating personalized savings plans.

The project uses the LlamaIndex framework and the open-weight Qwen3 4B language model, running locally through Ollama. This removes the need for paid LLM API access.

## 1. LLM Selection

- Model: Qwen3 4B
- Provider: Qwen (Alibaba)
- Runtime: Ollama
- Framework: LlamaIndex
- Deployment: Local model inference

### Why this model?

Qwen3 4B was selected because it is an open-weight language model that can run locally without requiring a paid API subscription.

It supports tool calling through Ollama, making it suitable for an agentic application that needs to select and execute Python functions.

Its relatively small model size also makes it a practical choice for experimentation in Google Colab.

## 2. Available Tools

### 1. parse_transactions
- Input: `file_content` (String)
- Output: Array of Objects
- Description: Extracts and structures financial transactions from uploaded CSV files.

### 2. categorize_transactions
- Input: `transactions` (Array of Objects)
- Output: Array of Objects
- Description: Categorizes transactions into Food, Housing, Transportation, Entertainment, Healthcare, Shopping, and Other.

### 3. calculate_financial_summary
- Inputs: `transactions`, `start_date`, `end_date`
- Output: Object
- Description: Calculates total income, expenses, savings, remaining balance, and spending distribution.

### 4. manage_budget
- Inputs: `category_budgets`, `period`
- Output: Object
- Description: Creates or updates spending limits for different categories.

### 5. analyze_budget_status
- Inputs: `actual_spending`, `budget_limits`
- Output: Object
- Description: Compares actual spending with budgets and identifies exceeded limits.

### 6. detect_anomalies
- Input: `transactions` (Array of Objects)
- Output: Array of Objects
- Description: Detects unusual transactions, unusually large expenses, and possible duplicate transactions.

### 7. calculate_savings_plan
- Inputs: `monthly_income`, `current_expenses`, `target_savings_rate`
- Output: Object
- Description: Calculates savings targets and the expense reductions needed to achieve them.

## 3. System Prompt

You are SmartSpend, an AI Personal Finance Agent.

Analyze financial transactions, categorize expenses, manage budgets, detect unusual spending, and create personalized savings plans.

Understand user requests, plan tasks, and select the appropriate tools.

Use Python tools for accurate financial calculations. Never invent financial data or treat anomaly flags as confirmed fraud.

Protect private information and never execute financial transactions.

Always prioritize accuracy, transparency, and user privacy.

## 4. Main Objectives

- Track income and expenses.
- Understand spending patterns.
- Manage monthly budgets.
- Detect unusual transactions.
- Calculate savings targets.
- Provide personalized financial recommendations.

## 5. Technology Stack

- Python
- LlamaIndex
- Qwen3 4B
- Ollama
- FunctionTool
- FunctionAgent
- Pandas
- Google Colab

## 6. Expected Workflow

1. Receive the user's financial request or transaction data.
2. Understand the user's goal.
3. Plan the required steps.
4. Select and execute the appropriate tools.
5. Analyze the returned results.
6. Present financial insights and recommendations.

## 7. Cost and Deployment

Qwen3 4B is an open-weight model and can be run locally using Ollama without paying for LLM API calls.

No Anthropic API key or paid LLM subscription is required.

The project can be tested in Google Colab using its available free computing resources, although hardware availability and runtime limits may affect performance.

## 8. Project Status

Project planning and agent design completed.

The implementation includes transaction-processing tools, financial analysis, budget management, anomaly detection, savings calculations, and LlamaIndex agent integration.

The complete workflow should be validated using sample financial data before final deployment.
