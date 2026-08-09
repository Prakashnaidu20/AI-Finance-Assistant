# 💰 AI Finance Assistant

### Personal Financial Analytics & Intelligent Budget Management Platform

<p align="center">
  <b>Track • Analyze • Budget • Invest • Understand</b>
</p>

---

## 📌 Overview

**AI Finance Assistant** is a personal financial analytics platform designed to help users understand and manage their finances through **data-driven insights and interactive visualizations**.

Unlike applications that use predefined or randomly generated financial data, this system allows users to enter their **actual income, expenses, investments, and budgets**. The application then automatically analyzes the provided data and presents meaningful financial insights.

The project combines **Python, SQL, Data Analytics, Interactive Visualization, and AI** into a single portfolio-ready application.

---

## 🎯 Problem Statement

Managing personal finances can be difficult when financial information is scattered across different sources.

Users often struggle to answer questions such as:

* Where am I spending the most?
* How much am I saving every month?
* Am I staying within my budget?
* How much am I investing?
* Which expense categories need attention?
* How has my spending changed over time?
* What does my current financial position look like?

**AI Finance Assistant** addresses these problems by converting raw financial transactions into understandable analytics and actionable insights.

---

## 🚀 Key Features

### 💵 Income Management

* Add salary and other income sources
* Record income with date and description
* Track total income over time

### 💳 Expense Management

* Record daily expenses
* Categorize spending
* Analyze category-wise expenses
* Identify highest spending categories

### 📈 Investment Tracking

* Record SIP contributions
* Track stocks, mutual funds, FD, gold and other investments
* Analyze investment allocation
* Monitor total investment contributions

### 🎯 Budget Management

* Create monthly category budgets
* Compare actual spending against budgets
* Calculate budget utilization
* Detect overspending

### 📊 Financial Analytics

Automatically calculates:

* Total Income
* Total Expenses
* Total Investments
* Savings
* Savings Rate
* Expense Ratio
* Investment Rate
* Financial Health Score

### 📉 Interactive Dashboard

The dashboard provides visual analytics for:

* Income vs Expenses
* Monthly Cash Flow
* Expense Distribution
* Category-wise Spending
* Budget vs Actual
* Investment Allocation
* Financial Health

### 🤖 AI Finance Assistant

Users can ask natural-language questions about their own financial data.

Example:

> **"Where did I spend the most?"**

> **"How much did I save?"**

> **"What is my savings rate?"**

> **"How much have I invested?"**

The assistant analyzes the stored financial data and generates easy-to-understand insights.

---

# 🏗️ System Architecture

```text
                 ┌──────────────────────┐
                 │        USER          │
                 └──────────┬───────────┘
                            │
                            ▼
              ┌─────────────────────────┐
              │    Streamlit Interface  │
              └────────────┬────────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
     Income Data      Expense Data    Investment Data
          │                │                │
          └────────────────┼────────────────┘
                           ▼
                  ┌─────────────────┐
                  │  SQLite Database│
                  └────────┬────────┘
                           │
                           ▼
                ┌────────────────────┐
                │ Python Analytics   │
                │      Engine        │
                └─────────┬──────────┘
                          │
          ┌───────────────┼────────────────┐
          ▼               ▼                ▼
       KPIs          Visualizations    Budget Analysis
          │               │                │
          └───────────────┼────────────────┘
                          ▼
                 ┌──────────────────┐
                 │   AI Assistant   │
                 └────────┬─────────┘
                          │
                          ▼
                  Financial Insights
```

---

# 🛠️ Technology Stack

| Technology       | Purpose                           |
| ---------------- | --------------------------------- |
| **Python**       | Core application and analytics    |
| **Pandas**       | Data processing and analysis      |
| **NumPy**        | Numerical operations              |
| **SQL / SQLite** | Financial data storage            |
| **Streamlit**    | Interactive web application       |
| **Plotly**       | Data visualization                |
| **Power BI**     | Advanced BI dashboard integration |
| **OpenAI API**   | Optional AI-powered analysis      |
| **Git & GitHub** | Version control and portfolio     |

---

# 📂 Project Structure

```text
AI_Finance_Assistant/
│
├── app.py
│   └── Streamlit application and user interface
│
├── database.py
│   └── Database creation and CRUD operations
│
├── analytics.py
│   └── Financial calculations and analytics
│
├── assistant.py
│   └── AI and rule-based finance assistant
│
├── schema.sql
│   └── Database schema
│
├── requirements.txt
│   └── Python dependencies
│
├── .env.example
│   └── Environment variable template
│
├── .gitignore
│   └── Git ignored files
│
└── README.md
    └── Project documentation
```

---

# ⚙️ Installation & Setup

## 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/AI-Finance-Assistant.git
```

Move into the project:

```bash
cd AI-Finance-Assistant
```

---

## 2️⃣ Create a virtual environment

### Windows

```bash
python -m venv .venv
```

### macOS / Linux

```bash
python3 -m venv .venv
```

---

## 3️⃣ Install dependencies

If PowerShell activation is restricted on Windows, you can install directly using:

```powershell
.venv\Scripts\python.exe -m pip install -r requirements.txt
```

Otherwise activate the environment normally:

```powershell
.venv\Scripts\activate
```

Then:

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Run the application

```bash
streamlit run app.py
```

The application will open in your browser.

Usually:

```text
http://localhost:8501
```

---

# 🧑‍💻 How To Use

### Step 1 — Add Income

Enter your actual income.

Example:

```text
Salary       ₹50,000
Freelancing  ₹10,000
```

### Step 2 — Add Expenses

Enter your real expenses.

Example:

```text
Food          ₹5,000
Rent         ₹12,000
Transport     ₹2,000
Shopping      ₹3,000
```

### Step 3 — Add Investments

Record your investments.

Example:

```text
SIP            ₹5,000
Stocks         ₹3,000
```

### Step 4 — Set Your Budget

Example:

```text
Food          ₹6,000
Transport     ₹3,000
Shopping      ₹4,000
Entertainment ₹2,000
```

### Step 5 — Analyze

The dashboard automatically calculates:

```text
Income
   ↓
Expenses
   ↓
Investments
   ↓
Savings
   ↓
Savings Rate
   ↓
Financial Health
```

---

# 📊 Dashboard Modules

## 1. Financial Overview

Displays:

* Total Income
* Total Expenses
* Investments
* Savings
* Savings Rate
* Financial Health Score
* Monthly Cash Flow

---

## 2. Expense Analytics

Provides:

* Category-wise spending
* Expense distribution
* Highest spending category
* Spending trends

---

## 3. Budget Analytics

Compares:

```text
Budget vs Actual Spending
```

and identifies categories where spending exceeds the planned budget.

---

## 4. Investment Analytics

Analyzes:

* Total investments
* Investment categories
* Investment allocation
* Contribution trends

---

## 5. AI Finance Assistant

Ask questions using natural language and receive insights based on your entered financial data.

---

# 🧮 Financial KPIs

### Savings

```text
Savings = Income - Expenses - Investments
```

### Savings Rate

```text
Savings Rate = (Savings / Income) × 100
```

### Expense Ratio

```text
Expense Ratio = (Expenses / Income) × 100
```

### Investment Rate

```text
Investment Rate = (Investments / Income) × 100
```

These metrics are calculated automatically by the application.

---

# 🔐 Data & Privacy

The application stores financial records locally using **SQLite**.

Sensitive configuration such as API keys should be stored in a `.env` file and should **never be committed to GitHub**.

The `.gitignore` file excludes:

```text
.env
finance.db
.venv/
```

---

# 📈 Future Enhancements

The project can be extended with:

* 🔐 User authentication
* ☁️ Cloud database
* 📱 Mobile-friendly interface
* 📥 CSV/Excel import
* 📤 Financial report export
* 📧 Monthly email reports
* 📊 Advanced Power BI dashboard
* 📈 Expense forecasting
* 🚨 Anomaly detection
* 🤖 Advanced conversational AI
* 🗃️ PostgreSQL integration
* 🐳 Docker deployment
* ☁️ Cloud deployment
* 📅 Recurring transaction management

---

# 🎓 Data Analyst Skills Demonstrated

This project demonstrates practical experience in:

```text
Python
SQL
Data Cleaning
Data Transformation
Exploratory Data Analysis
KPI Development
Financial Analytics
Data Visualization
Dashboard Development
Business Intelligence
Database Management
AI Integration
Git & GitHub
```

---

# 💼 Resume Description

**AI Finance Assistant & Personal Financial Analytics Platform**

> Developed a personal finance analytics platform using Python, SQL, Streamlit, and Plotly to analyze user-provided income, expenses, investments, and budgets. Implemented financial KPIs, budget-vs-actual analysis, spending analytics, investment tracking, financial health scoring, interactive dashboards, and an AI-powered natural-language assistant for data-driven financial insights.

---

# 🌟 Project Highlights

```text
✔ Real user financial data
✔ Interactive analytics dashboard
✔ SQL database integration
✔ Financial KPI calculations
✔ Budget monitoring
✔ Investment tracking
✔ Overspending detection
✔ AI-powered data analysis
✔ Modular Python architecture
✔ GitHub-ready project
```

---

# ⚠️ Disclaimer

This application is designed for **educational and analytical purposes**.

It provides calculations and insights based on user-provided data and should not be considered professional investment, tax, legal, or financial advice.

---

# 👨‍💻 Author

**Prakash Naidu**

B.Tech Computer Science & Engineering
Artificial Intelligence & Machine Learning

### Areas of Interest

`Data Analytics` • `Artificial Intelligence` • `Machine Learning` • `Python` • `SQL` • `Business Intelligence`

---

## ⭐ If you found this project useful

Give the repository a ⭐ and feel free to explore, improve, and customize the project.

**Built with Python, Data Analytics & AI. 🚀**
