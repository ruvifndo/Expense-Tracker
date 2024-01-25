import unittest
import json
from expense_tracker import save_expenses, load_expenses

class TestExpenseTracker(unittest.TestCase):

    def test_save_expenses_empty(self):
        expenses = []
        save_expenses(expenses)
        with open("expenses.json", "r") as file:
            data = json.load(file)
        self.assertEqual(data, [])

    def test_save_expenses_with_data(self):
        expenses = [{"description": "Groceries", "amount": 50.0, "date": "2023-11-21"}]
        save_expenses(expenses)
        with open("expenses.json", "r") as file:
            data = json.load(file)
        self.assertEqual(data, expenses)

    def test_load_expenses_empty_file(self):
        expenses = load_expenses()
        self.assertEqual(expenses, [])

    def test_load_expenses_with_data(self):
        with open("expenses.json", "w") as file:
            json.dump([{"description": "Coffee", "amount": 3.50, "date": "2023-11-20"}], file)
        expenses = load_expenses()
        self.assertEqual(expenses, [{"description": "Coffee", "amount": 3.50, "date": "2023-11-20"}])

# ... (add more tests for other functions)

if __name__ == "__main__":
    unittest.main()
