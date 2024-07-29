class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, description, amount):
        """Add a new expense."""
        expense = {'description': description, 'amount': amount}
        self.expenses.append(expense)

    def remove_expense(self, index):
        """Remove an expense by index."""
        if 0 <= index < len(self.expenses):
            del self.expenses[index]
        else:
            print("Invalid index. No expense removed.")

    def list_expenses(self):
        """List all expenses."""
        if not self.expenses:
            print("No expenses recorded.")
            return
        for i, expense in enumerate(self.expenses):
            print(f"{i + 1}. {expense['description']}: ${expense['amount']:.2f}")

def main():
    tracker = ExpenseTracker()

    while True:
        print("\nExpense Tracker")
        print("1. Add Expense")
        print("2. Remove Expense")
        print("3. List Expenses")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            description = input("Enter expense description: ")
            amount = float(input("Enter expense amount: "))
            tracker.add_expense(description, amount)
            print("Expense added.")
        elif choice == '2':
            tracker.list_expenses()
            index = int(input("Enter the number of the expense to remove: ")) - 1
            tracker.remove_expense(index)
            print("Expense removed.")
        elif choice == '3':
            tracker.list_expenses()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please choose a number between 1 and 4.")

if __name__ == "__main__":
    main()
