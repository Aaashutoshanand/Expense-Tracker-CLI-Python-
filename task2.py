import csv
import os

FILE_NAME = "expenses.csv"

# Ensure file exists
def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["Description", "Amount"])

# Add expense
def add_expense():
    desc = input("Enter expense description: ")
    amount = input("Enter amount: ")

    with open(FILE_NAME, "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([desc, amount])

    print(" Expense added successfully!")

# View all expenses
def view_expenses():
    print("\n All Expenses:\n")
    try:
        with open(FILE_NAME, "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for row in reader:
                print(f"• {row[0]} → ₹{row[1]}")
    except FileNotFoundError:
        print(" No expenses found.")

# Calculate total
def total_expenses():
    total = 0
    try:
        with open(FILE_NAME, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                total += float(row[1])

        print(f"\n Total Expenses: ₹{total}")
    except FileNotFoundError:
        print(" No expenses to calculate.")

# Menu system
def menu():
    initialize_file()

    while True:
        print("\n====== Expense Tracker ======")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expenses")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            total_expenses()
        elif choice == "4":
            print(" Exiting... Goodbye!")
            break
        else:
            print(" Invalid choice, try again!")

# Run program
menu()