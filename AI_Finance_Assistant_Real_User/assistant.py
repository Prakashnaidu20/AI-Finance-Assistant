import os

def local_answer(question, df, metrics):
    q = question.lower()

    expenses = df[df["type"] == "Expense"]
    investments = df[df["type"] == "Investment"]

    if ("most" in q or "highest" in q) and ("spend" in q or "expense" in q):
        if expenses.empty:
            return "You have not entered any expenses yet."

        top = (
            expenses.groupby("category")["amount"]
            .sum()
            .sort_values(ascending=False)
        )

        return (
            f"Your highest spending category is **{top.index[0]}** "
            f"with **₹{top.iloc[0]:,.0f}**."
        )

    if "save" in q or "saving" in q:
        return (
            f"Based on your entered data:\n\n"
            f"- Income: **₹{metrics['income']:,.0f}**\n"
            f"- Expenses: **₹{metrics['expenses']:,.0f}**\n"
            f"- Investments: **₹{metrics['investments']:,.0f}**\n"
            f"- Remaining savings: **₹{metrics['savings']:,.0f}**\n"
            f"- Savings rate: **{metrics['savings_rate']:.1f}%**"
        )

    if "invest" in q:
        return (
            f"You have entered **₹{metrics['investments']:,.0f}** "
            "as investment contributions."
        )

    if "income" in q:
        return f"Your total entered income is **₹{metrics['income']:,.0f}**."

    if "expense" in q or "spend" in q:
        return f"Your total entered expenses are **₹{metrics['expenses']:,.0f}**."

    return (
        f"I analyzed your entered data.\n\n"
        f"**Income:** ₹{metrics['income']:,.0f}\n\n"
        f"**Expenses:** ₹{metrics['expenses']:,.0f}\n\n"
        f"**Investments:** ₹{metrics['investments']:,.0f}\n\n"
        f"**Savings:** ₹{metrics['savings']:,.0f}\n\n"
        f"**Savings rate:** {metrics['savings_rate']:.1f}%"
    )

def answer_question(question, df, metrics):
    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return local_answer(question, df, metrics)

    try:
        from openai import OpenAI

        client = OpenAI(api_key=api_key)

        summary = {
            "income": round(metrics["income"], 2),
            "expenses": round(metrics["expenses"], 2),
            "investments": round(metrics["investments"], 2),
            "savings": round(metrics["savings"], 2),
            "savings_rate": round(metrics["savings_rate"], 2)
        }

        prompt = f"""
You are a finance data analytics assistant.

Analyze only the user's supplied financial summary.
Do not invent transactions.
Do not provide personalized regulated investment, tax, legal, or financial advice.
Give concise educational explanations.

User question:
{question}

Financial summary:
{summary}
"""

        response = client.responses.create(
            model=os.getenv("OPENAI_MODEL", "gpt-5.4-mini"),
            input=prompt
        )

        return response.output_text

    except Exception:
        return local_answer(question, df, metrics)
