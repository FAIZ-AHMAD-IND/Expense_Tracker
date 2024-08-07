import os
import csv
from datetime import datetime

class Expense:
    def __init__(self, amount, description, category, date):
        self.amount = amount
        self.description = description
        self.category = category
        self.date = date

def get_current_date():
    return datetime.now().strftime("%Y-%m-%d")

def add_expense(expenses):
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    category = input("Enter category (e.g., food, transportation, entertainment): ")
    date = get_current_date()
    expenses.append(Expense(amount, description, category, date))
    print("Expense added successfully.")

def save_expenses(expenses):
    with open("expenses.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Amount", "Description", "Category", "Date"])
        for expense in expenses:
            writer.writerow([expense.amount, expense.description, expense.category, expense.date])

def load_expenses():
    expenses = []
    if os.path.exists("expenses.csv"):
        with open("expenses.csv", mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                expenses.append(Expense(float(row["Amount"]), row["Description"], row["Category"], row["Date"]))
    return expenses

def display_expenses(expenses):
    print(f"{'Amount':<10} {'Description':<20} {'Category':<20} {'Date':<15}")
    for expense in expenses:
        print(f"{expense.amount:<10} {expense.description:<20} {expense.category:<20} {expense.date:<15}")

def analyze_expenses(expenses):
    category_totals = {}
    monthly_totals = {}
    for expense in expenses:
        if expense.category in category_totals:
            category_totals[expense.category] += expense.amount
        else:
            category_totals[expense.category] = expense.amount
        
        month = expense.date[:7]
        if month in monthly_totals:
            monthly_totals[month] += expense.amount
        else:
            monthly_totals[month] = expense.amount

    print("\nCategory-wise Expenditure:")
    for category, total in category_totals.items():
        print(f"{category}: {total}")

    print("\nMonthly Expenditure:")
    for month, total in monthly_totals.items():
        print(f"{month}: {total}")

def main():
    expenses = load_expenses()
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Analyze Expenses")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_expense(expenses)
            save_expenses(expenses)
        elif choice == '2':
            display_expenses(expenses)
        elif choice == '3':
            analyze_expenses(expenses)
        elif choice == '4':
            print("Exiting Expense Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

main()
