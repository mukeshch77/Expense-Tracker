import pandas as pd
import os
from tabulate import tabulate

# Initialize an empty DataFrame with relevant columns
columns = ['Date', 'Category', 'Description', 'Amount']
expenses_df = pd.DataFrame(columns=columns)

# Function to add a new expense
def add_expense(date, category, description, amount):
    global expenses_df
    expense = pd.DataFrame([[date, category, description, amount]], columns=columns)
    expenses_df = pd.concat([expenses_df, expense], ignore_index=True)
    print(f"\033[1;35mExpense Added: {category} - ${amount}\033[0m")  # Purple text

# Function to display all expenses
def view_expenses():
    if expenses_df.empty:
        print("\033[1;90mNo expenses recorded yet.\033[0m")  # Gray text
    else:
        print("\033[1;37mExpense Report:\033[0m")  # White text
        print(tabulate(expenses_df, headers='keys', tablefmt='pretty', showindex=False))

# Function to generate a summary of expenses by category
def generate_report():
    if expenses_df.empty:
        print("\033[1;90mNo expenses recorded yet to generate a report.\033[0m")  # Gray text
        return
    
    summary = expenses_df.groupby('Category').agg({'Amount': 'sum'}).reset_index()
    print("\033[1;37mExpense Summary by Category:\033[0m")  # White text
    print(tabulate(summary, headers='keys', tablefmt='pretty', showindex=False))

# Function to save expenses to a CSV file
def save_expenses(filename="expenses.csv"):
    expenses_df.to_csv(filename, index=False)
    print(f"\033[1;35mExpenses saved to {filename}\033[0m")  # Purple text

# Function to load expenses from a CSV file
def load_expenses(filename="expenses.csv"):
    global expenses_df
    if os.path.exists(filename):
        expenses_df = pd.read_csv(filename)
        print(f"\033[1;35mExpenses loaded from {filename}\033[0m")  # Purple text
    else:
        print(f"\033[1;90mNo file found. Starting fresh.\033[0m")  # Gray text

# Main menu
def main_menu():
    while True:
        print("\n\033[1;37mExpense Tracker Application\033[0m")  
        print("\033[1;37m1. Add Expense\033[0m")
        print("\033[1;37m2. View Expenses\033[0m")
        print("\033[1;37m3. Generate Report\033[0m")
        print("\033[1;37m4. Save Expenses\033[0m")
        print("\033[1;37m5. Load Expenses\033[0m")
        print("\033[1;37m6. Exit\033[0m")

        choice = input("\n\033[1;37mEnter your choice: \033[0m")

        if choice == '1':
            date = input("Enter date (YYYY-MM-DD): ")
            category = input("Enter category: ")
            description = input("Enter description: ")
            amount = float(input("Enter amount: $"))
            add_expense(date, category, description, amount)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            generate_report()
        elif choice == '4':
            filename = input("Enter filename to save expenses (default 'expenses.csv'): ")
            if filename == "":
                filename = "expenses.csv"
            save_expenses(filename)
        elif choice == '5':
            filename = input("Enter filename to load expenses (default 'expenses.csv'): ")
            if filename == "":
                filename = "expenses.csv"
            load_expenses(filename)
        elif choice == '6':
            print("\033[1;90mExiting... Goodbye!\033[0m")  
            break
        else:
            print("\033[1;90mInvalid choice. Please try again.\033[0m") 

# Run the application
if __name__ == "__main__":
    main_menu()
