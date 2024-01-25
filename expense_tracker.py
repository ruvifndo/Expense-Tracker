import json
from datetime import datetime

def save_expenses(expenses):
    """Saves expenses to a JSON file."""
    try:
        with open("expenses.json", "w") as file:
            json.dump(expenses, file, indent=4)
        print("Expenses saved successfully!")
    except Exception as e:
        print("Error saving expenses:", e)

def load_expenses():
    """Loads expenses from a JSON file."""
    try:
        with open("expenses.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if file doesn't exist
    except Exception as e:
        print("Error loading expenses:", e)
        return []

def add_expense():
    """Adds a new expense."""
    try:
        description = input("Enter expense description: ")
        amount = float(input("Enter expense amount: "))

        while True:
            date_str = input("Enter expense date (YYYY-MM-DD): ")
            try:
                date = datetime.strptime(date_str, "%Y-%m-%d").date()
                break  # Date parsed successfully
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD (e.g., 2023-11-21).")

        expenses = load_expenses()
        expenses.append({"description": description, "amount": amount, "date": date.strftime("%Y-%m-%d")})
        save_expenses(expenses)
        print("Expense added successfully!")
    except ValueError:
        print("Invalid amount entered. Please enter a numerical value.")

def view_expenses():
    """Displays all saved expenses."""
    try:
        expenses = load_expenses()
        if expenses:
            print("Expenses:")
            i=0
            for expense in expenses:
                
                print(f" {i}. Description: {expense['description']}")
                print(f"  Amount: ${expense['amount']:.2f}")
                print(f"  Date: {expense['date']}")
                i+=1
        else:
            print("No expenses found.")
    except Exception as e:
        print("Error displaying expenses:", e)

def edit_expense():
    """Edits an existing expense."""
    try:
        expenses = load_expenses()
        expense_index = int(input("Enter the index of the expense to edit (starting from 0): "))
        if 0 <= expense_index < len(expenses):
            try:
                description = input("Enter new expense description (leave blank to keep current): ")
                amount_str = input("Enter new expense amount (leave blank to keep current): ")

                if amount_str:
                    amount = float(amount_str)
                else:
                    amount = expenses[expense_index]["amount"]

                while True:
                    date_str = input("Enter new expense date (YYYY-MM-DD) (leave blank to keep current): ")
                    if not date_str:
                        break  # Keep current date
                    try:
                        date = datetime.strptime(date_str, "%Y-%m-%d").date()
                        break  # Date parsed successfully
                    except ValueError:
                        print("Invalid date format. Please use YYYY-MM-DD (e.g., 2023-11-21).")

                if description:
                    expenses[expense_index]["description"] = description
                expenses[expense_index]["amount"] = amount
                if date_str:
                    expenses[expense_index]["date"] = date.strftime("%Y-%m-%d")

                save_expenses(expenses)
                print("Expense edited successfully!")
            except ValueError:
                print("Invalid amount entered. Please enter a numerical value.")
        else:
            print("Invalid expense index.")
    except Exception as e:
        print("Error editing expense:", e)

def delete_expense():
    """Deletes an expense."""
    try:
        expenses = load_expenses()
        expense_index = int(input("Enter the index of the expense to delete (starting from 0): "))
        if 0 <= expense_index < len(expenses):
            del expenses[expense_index]
            save_expenses(expenses)
            print("Expense deleted successfully!")
        else:
            print("Invalid expense index.")
    except Exception as e:
        print("Error deleting expense:", e)


if __name__ == "__main__":
    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. Edit expense")
        print("4. Delete expense")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            edit_expense()
        elif choice == "4":
            delete_expense()
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
