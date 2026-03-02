import pandas as pd
import os
from datetime import datetime

DATA_FILE = "data/expenses.csv"

def add_expense(amount, category, description):
    date = datetime.now().strftime("%Y-%m-%d")

    new_data = {
        "Date": date,
        "Amount": amount,
        "Category": category,
        "Description": description
    }

    df_new = pd.DataFrame([new_data])

    if os.path.exists(DATA_FILE):
        df_existing = pd.read_csv(DATA_FILE)
        df_combined = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_combined = df_new

    df_combined.to_csv(DATA_FILE, index=False)

    print("Expense added successfully!")