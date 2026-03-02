# Smart Expense Tracker with Insights

An intermediate-level Python CLI project that helps users log expenses, analyze spending patterns, and generate financial insights using data visualization.

This project goes beyond simple expense logging by including analytics, summaries, and prediction features.

---

## Features

- Add and store expenses in CSV format
- Automatic data persistence
- Category-wise spending breakdown
- Visual spending analysis using matplotlib
- Monthly spending estimation
- Modular and clean code structure
- Git branch workflow implementation

---

## Tech Stack

- Python 3.x
- Pandas
- Matplotlib
- Git & GitHub (Feature branch workflow)

---

## Project Structure

smart-expense-tracker/
- data/
   - expenses.csv (auto generated)
   - sample.txt
- reports/
  - sample.txt
- expense_manager.py
- insights.py
- main.py
- README.md
- requirements.txt

---

## How To Run

### 1️⃣ Clone the repository
git clone https://github.com/AkshraThareja/smart-expense-tracker.git

cd smart-expense-tracker

### 2️⃣ Create virtual environment (Windows)
python -m venv venv
venv\Scripts\activate

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Run the program
python main.py

---

## How It Works

Expenses are stored in CSV format using pandas.  
The insights module:

- Calculates total spending
- Groups spending by category
- Generates a bar chart visualization
- Estimates next month’s expenses using simple growth logic

---

## Git Workflow Used

This project follows a feature-branch development approach:

- main branch for stable code
- feature branches for new additions
- Pull Requests for controlled merges

---

## Learning Outcomes

This project helped strengthen:

- Modular Python design
- Data manipulation with pandas
- Data visualization
- Git branching workflow
- Project structuring for scalability

---

## Future Improvements

- Automatic category detection
- Export monthly reports as PDF
- Budget tracking system
- Interactive dashboard (Streamlit version)

---

Built with focus on structured thinking and clean implementation.
