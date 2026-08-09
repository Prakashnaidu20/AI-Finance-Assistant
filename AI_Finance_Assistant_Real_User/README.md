# AI Finance Assistant — Real User Version

A personal finance analytics application where the user enters their own income, expenses, investments and budgets.

## Important

This version DOES NOT automatically generate financial amounts.

The dashboard starts empty.

All analysis comes from data entered by the user.

## Features

- Add Income
- Add Expenses
- Add Investments
- Set monthly budgets
- Income vs expense dashboard
- Savings calculation
- Savings rate
- Financial health score
- Expense category analysis
- Budget vs actual
- Investment allocation
- AI finance Q&A
- SQLite local database
- Optional OpenAI integration
- Delete all local data

## Run in VS Code

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

Install:

```bash
pip install -r requirements.txt
```

Run:

```bash
streamlit run app.py
```

## First use

1. Open the application.
2. Add your salary/income.
3. Add your actual expenses.
4. Add your investments.
5. Set your monthly budgets.
6. Open Overview.
7. Open Expenses.
8. Open Budgets.
9. Open Investments.
10. Ask questions in AI Assistant.

## Optional AI

Copy `.env.example` to `.env` and add your API key.

The application remains functional without an API key because it includes a local analytics assistant.

## Resume positioning

**AI Finance Assistant & Personal Financial Analytics Platform**

Python | Pandas | SQL/SQLite | Streamlit | Plotly | Power BI-ready | AI

Do not claim financial savings or business impact unless you actually measured them.
