import sqlite3
from pathlib import Path
import pandas as pd

DB_PATH = Path("finance.db")

def get_conn():
    return sqlite3.connect(DB_PATH)

def init_db():
    conn = get_conn()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS transactions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            type TEXT NOT NULL CHECK(type IN ('Income','Expense','Investment')),
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            description TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS budgets (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            month TEXT NOT NULL,
            category TEXT NOT NULL,
            amount REAL NOT NULL,
            UNIQUE(month, category)
        )
    """)

    conn.commit()
    conn.close()

def add_transaction(date, t_type, category, amount, description):
    conn = get_conn()
    conn.execute(
        """INSERT INTO transactions
           (date, type, category, amount, description)
           VALUES (?, ?, ?, ?, ?)""",
        (date, t_type, category, float(amount), description)
    )
    conn.commit()
    conn.close()

def get_transactions():
    conn = get_conn()
    df = pd.read_sql_query(
        "SELECT * FROM transactions ORDER BY date DESC, id DESC",
        conn
    )
    conn.close()

    if not df.empty:
        df["date"] = pd.to_datetime(df["date"])

    return df

def delete_transaction(transaction_id):
    conn = get_conn()
    conn.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    conn.commit()
    conn.close()

def upsert_budget(month, category, amount):
    conn = get_conn()
    conn.execute("""
        INSERT INTO budgets(month, category, amount)
        VALUES (?, ?, ?)
        ON CONFLICT(month, category)
        DO UPDATE SET amount = excluded.amount
    """, (month, category, float(amount)))
    conn.commit()
    conn.close()

def get_budgets():
    conn = get_conn()
    df = pd.read_sql_query(
        "SELECT * FROM budgets ORDER BY month DESC, category",
        conn
    )
    conn.close()
    return df

def clear_all_data():
    conn = get_conn()
    conn.execute("DELETE FROM transactions")
    conn.execute("DELETE FROM budgets")
    conn.commit()
    conn.close()
