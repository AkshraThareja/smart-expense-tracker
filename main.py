from expense_manager import add_expense

def main():
    while True:
        print("\n--- Smart Expense Tracker ---")
        print("1. Add Expense")
        print("2. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category (Food/Travel/Other): ")
            description = input("Enter description: ")

            add_expense(amount, category, description)

        elif choice == "2":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()