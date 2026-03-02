from insights import show_summary
from expense_manager import add_expense

def main():
    while True:
        print("\n--- Smart Expense Tracker ---")
        print("1. Add Expense")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category (Food/Travel/Rent/Electricity Bill/Other): ")
            description = input("Enter description: ")

            add_expense(amount, category, description)

        elif choice == "2":
            show_summary()

        elif choice == "3":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()