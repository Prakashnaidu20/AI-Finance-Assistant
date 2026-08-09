import pandas as pd
import plotly.express as px
import streamlit as st
from database import (
    init_db, add_transaction, get_transactions, delete_transaction,
    upsert_budget, get_budgets, clear_all_data
)
from analytics import (
    calculate_metrics, monthly_summary, category_summary,
    budget_summary, financial_health_score, investment_summary
)
from assistant import answer_question

st.set_page_config(page_title="AI Finance Assistant", page_icon="💰", layout="wide")
init_db()

st.title("💰 AI Finance Assistant")
st.caption("Enter your own financial data. The dashboard analyzes only the information you provide.")

# ---------------- SIDEBAR ----------------
with st.sidebar:
    st.header("➕ Add Financial Data")

    entry_type = st.radio(
        "What do you want to add?",
        ["Income", "Expense", "Investment"],
        horizontal=False
    )

    entry_date = st.date_input("Date", pd.Timestamp.today().date())
    amount = st.number_input("Amount (₹)", min_value=0.01, step=100.0)

    if entry_type == "Income":
        category = st.selectbox("Income Source", ["Salary", "Freelancing", "Business", "Interest", "Other"])
    elif entry_type == "Expense":
        category = st.selectbox(
            "Expense Category",
            ["Food", "Transport", "Housing", "Utilities", "Shopping",
             "Health", "Education", "Entertainment", "Bills", "Other"]
        )
    else:
        category = st.selectbox(
            "Investment Type",
            ["SIP", "Stocks", "Mutual Funds", "FD", "Gold", "Crypto", "Other"]
        )

    description = st.text_input("Description", placeholder="e.g. Monthly salary / Grocery shopping")

    if st.button(f"Add {entry_type}", type="primary", use_container_width=True):
        add_transaction(str(entry_date), entry_type, category, amount, description)
        st.success(f"{entry_type} added successfully.")
        st.rerun()

    st.divider()

    st.header("🎯 Set Budget")
    budget_month = st.text_input(
        "Month",
        value=pd.Timestamp.today().strftime("%Y-%m"),
        help="Use YYYY-MM format"
    )
    budget_category = st.selectbox(
        "Budget Category",
        ["Food", "Transport", "Housing", "Utilities", "Shopping",
         "Health", "Education", "Entertainment", "Bills", "Other"]
    )
    budget_amount = st.number_input("Monthly Budget (₹)", min_value=0.0, step=500.0)

    if st.button("Save Budget", use_container_width=True):
        if len(budget_month) == 7 and budget_month[4] == "-":
            upsert_budget(budget_month, budget_category, budget_amount)
            st.success("Budget saved.")
            st.rerun()
        else:
            st.error("Enter month as YYYY-MM.")

    st.divider()

    with st.expander("⚠️ Data Management"):
        st.caption("This permanently removes all locally stored transactions and budgets.")
        if st.button("Delete All My Data", use_container_width=True):
            clear_all_data()
            st.success("All data deleted.")
            st.rerun()

# ---------------- DATA ----------------
transactions = get_transactions()
budgets = get_budgets()

if transactions.empty:
    st.info(
        "👋 Welcome! Your dashboard is currently empty.\n\n"
        "Use the sidebar to add your real income, expenses, and investments."
    )
    st.subheader("Start by entering:")
    c1, c2, c3 = st.columns(3)
    c1.info("💵 Income\nSalary, freelancing, business income, etc.")
    c2.warning("💳 Expenses\nFood, rent, travel, shopping, bills, etc.")
    c3.success("📈 Investments\nSIP, stocks, mutual funds, FD, etc.")
    st.stop()

metrics = calculate_metrics(transactions)
health = financial_health_score(metrics)

# ---------------- KPI CARDS ----------------
c1, c2, c3, c4, c5 = st.columns(5)
c1.metric("Total Income", f"₹{metrics['income']:,.0f}")
c2.metric("Total Expenses", f"₹{metrics['expenses']:,.0f}")
c3.metric("Savings", f"₹{metrics['savings']:,.0f}")
c4.metric("Savings Rate", f"{metrics['savings_rate']:.1f}%")
c5.metric("Health Score", f"{health}/100")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📊 Overview", "💳 Expenses", "🎯 Budgets", "📈 Investments", "🤖 AI Assistant"
])

# ---------------- OVERVIEW ----------------
with tab1:
    st.subheader("Monthly Cash Flow")
    ms = monthly_summary(transactions)

    if not ms.empty:
        fig = px.bar(
            ms, x="month", y=["income", "expenses"],
            barmode="group", title="Income vs Expenses"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.subheader("Financial Health")
    st.progress(health / 100)

    if health >= 80:
        st.success("Strong financial position based on your entered data.")
    elif health >= 60:
        st.info("Moderate financial position. Review your spending and savings.")
    else:
        st.warning("Your current numbers indicate that spending deserves attention.")

    st.subheader("Recent Transactions")
    display_df = transactions.sort_values("date", ascending=False).head(10).copy()
    display_df["date"] = display_df["date"].dt.strftime("%Y-%m-%d")
    st.dataframe(display_df, use_container_width=True, hide_index=True)

# ---------------- EXPENSES ----------------
with tab2:
    expenses = transactions[transactions["type"] == "Expense"]

    if expenses.empty:
        st.info("Add expense records to see expense analytics.")
    else:
        cs = category_summary(transactions)
        left, right = st.columns(2)

        with left:
            fig = px.pie(
                cs, names="category", values="amount",
                hole=0.45, title="Expense Distribution"
            )
            st.plotly_chart(fig, use_container_width=True)

        with right:
            fig = px.bar(
                cs.sort_values("amount"), x="amount", y="category",
                orientation="h", title="Spending by Category"
            )
            st.plotly_chart(fig, use_container_width=True)

        st.dataframe(cs, use_container_width=True, hide_index=True)

# ---------------- BUDGETS ----------------
with tab3:
    bs = budget_summary(transactions, budgets)

    if bs.empty:
        st.info("No budgets configured yet. Set a budget from the sidebar.")
    else:
        fig = px.bar(
            bs, x="category", y=["budget", "actual"],
            barmode="group", title="Budget vs Actual"
        )
        st.plotly_chart(fig, use_container_width=True)

        over = bs[bs["actual"] > bs["budget"]]
        if not over.empty:
            st.warning(
                "⚠️ Overspending detected in: " +
                ", ".join(over["category"].astype(str).tolist())
            )

        st.dataframe(bs, use_container_width=True, hide_index=True)

# ---------------- INVESTMENTS ----------------
with tab4:
    inv = investment_summary(transactions)

    if inv.empty:
        st.info("Add investment records to see investment analytics.")
    else:
        left, right = st.columns(2)

        with left:
            fig = px.pie(
                inv, names="category", values="amount",
                hole=0.45, title="Investment Allocation"
            )
            st.plotly_chart(fig, use_container_width=True)

        with right:
            fig = px.bar(
                inv.sort_values("amount"), x="amount", y="category",
                orientation="h", title="Investment Contributions"
            )
            st.plotly_chart(fig, use_container_width=True)

        st.metric("Total Invested", f"₹{inv['amount'].sum():,.0f}")
        st.dataframe(inv, use_container_width=True, hide_index=True)

# ---------------- AI ASSISTANT ----------------
with tab5:
    st.subheader("🤖 Ask Your Finance Data")

    st.markdown(
        """
        Ask questions about **your own entered data**.

        Examples:
        - Where did I spend the most?
        - How much did I save?
        - What is my savings rate?
        - Which expenses are increasing?
        - How much have I invested?
        """
    )

    question = st.text_input("Ask a question")

    if st.button("Analyze My Data", type="primary") and question:
        with st.spinner("Analyzing your financial data..."):
            response = answer_question(question, transactions, metrics)
        st.markdown(response)

st.divider()
st.caption(
    "Educational analytics only. This application does not provide regulated investment, "
    "tax, legal, or personalized financial advice."
)
