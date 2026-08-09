import pandas as pd

def calculate_metrics(df):
    income = df.loc[df["type"] == "Income", "amount"].sum()
    expenses = df.loc[df["type"] == "Expense", "amount"].sum()
    investments = df.loc[df["type"] == "Investment", "amount"].sum()

    savings = income - expenses - investments
    savings_rate = (savings / income * 100) if income else 0
    expense_ratio = (expenses / income * 100) if income else 0
    investment_rate = (investments / income * 100) if income else 0

    return {
        "income": income,
        "expenses": expenses,
        "investments": investments,
        "savings": savings,
        "savings_rate": savings_rate,
        "expense_ratio": expense_ratio,
        "investment_rate": investment_rate
    }

def monthly_summary(df):
    x = df.copy()
    x["month"] = x["date"].dt.to_period("M").astype(str)

    income = (
        x[x["type"] == "Income"]
        .groupby("month")["amount"].sum()
    )

    expenses = (
        x[x["type"] == "Expense"]
        .groupby("month")["amount"].sum()
    )

    investments = (
        x[x["type"] == "Investment"]
        .groupby("month")["amount"].sum()
    )

    out = pd.DataFrame({
        "income": income,
        "expenses": expenses,
        "investments": investments
    }).fillna(0).reset_index()

    return out

def category_summary(df):
    return (
        df[df["type"] == "Expense"]
        .groupby("category", as_index=False)["amount"]
        .sum()
        .sort_values("amount", ascending=False)
    )

def investment_summary(df):
    return (
        df[df["type"] == "Investment"]
        .groupby("category", as_index=False)["amount"]
        .sum()
        .sort_values("amount", ascending=False)
    )

def budget_summary(transactions, budgets):
    if budgets.empty:
        return pd.DataFrame()

    x = transactions[transactions["type"] == "Expense"].copy()
    x["month"] = x["date"].dt.to_period("M").astype(str)

    actual = (
        x.groupby(["month", "category"], as_index=False)["amount"]
        .sum()
    )

    out = budgets.merge(
        actual,
        on=["month", "category"],
        how="left",
        suffixes=("_budget", "_actual")
    )

    out = out.rename(columns={
        "amount_budget": "budget",
        "amount_actual": "actual"
    })

    out["actual"] = out["actual"].fillna(0)
    out["variance"] = out["budget"] - out["actual"]
    out["utilization_pct"] = (
        out["actual"] / out["budget"] * 100
    ).where(out["budget"] > 0, 0)

    return out

def financial_health_score(metrics):
    if metrics["income"] <= 0:
        return 0

    score = 50

    savings_rate = metrics["savings_rate"]

    if savings_rate >= 30:
        score += 30
    elif savings_rate >= 20:
        score += 20
    elif savings_rate >= 10:
        score += 10
    elif savings_rate < 0:
        score -= 25

    if metrics["investment_rate"] >= 15:
        score += 10
    elif metrics["investment_rate"] >= 5:
        score += 5

    if metrics["expense_ratio"] > 90:
        score -= 15
    elif metrics["expense_ratio"] > 75:
        score -= 5

    return int(max(0, min(100, score)))
