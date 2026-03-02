import pandas as pd
import matplotlib.pyplot as plt
import os

DATA_FILE = "data/expenses.csv"

def show_summary():
    if not os.path.exists(DATA_FILE) or os.path.getsize(DATA_FILE) == 0:
        print("No expenses found.")
        return

    df = pd.read_csv(DATA_FILE)

    print("\nTotal Spending:", df["Amount"].sum())
    print("\nSpending by Category:")
    print(df.groupby("Category")["Amount"].sum())

    df.groupby("Category")["Amount"].sum().plot(kind="bar")
    plt.title("Spending by Category")
    plt.xlabel("Category")
    plt.ylabel("Amount")
    plt.show()

def predict_next_month():
    try:
        df = pd.read_csv(DATA_FILE)
    except FileNotFoundError:
        print("No data available.")
        return

    monthly_total = df["Amount"].sum()
    print("\nEstimated spending next month:", round(monthly_total * 1.05, 2))