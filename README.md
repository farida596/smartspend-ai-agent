# SmartSpend – AI Personal Finance Agent

SmartSpend is an AI-powered personal finance agent designed to help users manage their money by analyzing financial transactions, categorizing expenses, monitoring budgets, detecting unusual spending, and creating personalized savings plans.

## 1. LLM Selection

- Model: Claude Sonnet 4.5
- Provider: Anthropic

Why this model?

Claude Sonnet 4.5 was selected for its strong reasoning, mathematical capabilities, multi-step task handling, and tool-calling support. These capabilities allow the agent to analyze financial data, make decisions, use external tools, and provide personalized recommendations.

## 2. Available Tools

### 1. parse_transactions
- Input Name: `file_content`
- Input Type: String
- Output Type: Array of Objects
- Description: Extracts and structures financial transactions from uploaded CSV files.

### 2. categorize_transactions
- Input Name: `transactions`
- Input Type: Array of Objects
- Output Type: Array of Objects
- Description: Categorizes transactions into Food, Housing, Transportation, Entertainment, Healthcare, and Shopping.

### 3. calculate_financial_summary
- Input Names: `transactions`, `start_date`, `end_date`
- Input Types: Array of Objects, String, String
- Output Type: Object
- Description: Calculates total income, expenses, savings, remaining balance, and spending distribution.

### 4. manage_budget
- Input Names: `category_budgets`, `period`
- Input Types: Object, String
- Output Type: Object
- Description: Creates or updates spending limits for different categories.

### 5. analyze_budget_status
- Input Names: `actual_spending`, `budget_limits`
- Input Types: Object, Object
- Output Type: Object
- Description: Compares actual spending with budgets and identifies exceeded limits.

### 6. detect_anomalies
- Input Name: `transactions`
- Input Type: Array of Objects
- Output Type: Array of Objects
- Description: Detects unusual transactions and unexpected spending patterns.

### 7. calculate_savings_plan
- Input Names: `monthly_income`, `current_expenses`, `target_savings_rate`
- Input Types: Number, Number, Number
- Output Type: Object
- Description: Calculates savings targets and the expense reductions needed to achieve them.

## 3. System Prompt

You are SmartSpend, an AI Personal Finance Agent. Analyze transactions, categorize expenses, manage budgets, detect unusual spending, and create savings plans. Understand user requests, plan tasks, and use appropriate tools. Provide accurate financial insights and practical recommendations. Never invent financial data, expose private information, or execute financial transactions. Always prioritize accuracy, transparency, and user privacy.

## 4. Main Objectives

- Track income and expenses.
- Understand spending patterns.
- Manage monthly budgets.
- Detect unusual transactions.
- Calculate savings targets.
- Provide personalized financial recommendations.

## 5. Expected Workflow

1. Receive the user's financial request or transaction data.
2. Understand the user's goal.
3. Plan the required steps.
4. Select and execute the appropriate tools.
5. Analyze the returned results.
6. Present financial insights and recommendations.

## 6. Project Status

Project planning and agent design completed. Tool implementation and LLM integration are the next steps.
