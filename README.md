# Expense-Tracker
Build an application that tracks expenses and generates reports.

## Overview
This expense tracking app helps you track your expenses by recording relevant details such as date, category, description, and amount. You can also view all your expenses. Create summary reports by category Save your data as a CSV file and load previous data from the CSV file.

## feature

- **Add Expense:** Record a new expense with date, category, description, and amount.
- **View expenses:** View a list of all recorded expenses.
- **Create report:** Get a summary of expenses by category.
- **Record expenses:** Record recorded expenses as a CSV file.
- **Load expenses:** Load previously saved expenses from a CSV file.
- **Exit:** Exit the application.

## Instructions for use

### 1. Add costs
- Select option **1** from the main menu.
- Enter the spending date in the format "YYYY-MM-DD"
- Enter a category (e.g. "Food", "Transportation", etc.)
- Enter a brief description (optional).
- Enter the amount of expenses

example:
Enter date (YYYY-MM-DD): 2024-11-2
Enter category: Food
Fill in the details: Have lunch at the cafe.
Enter amount: $15.50
-

### 2. View expenses
- Select option **2** from the main menu to display all recorded expenses.

Production example:
Expense Report:
+------------+------------+--------------------+--------+
|    Date    |  Category  |     Description    | Amount |
+------------+------------+--------------------+--------+
| 2024-11-22 |    Food    | Lunch at Cafe      |  15.50 |
+------------+------------+--------------------+--------+


### 3. Generate report
- Select option **3** to create a summary of expenses by category. It shows the total amount used in each category.

Expense Summary by Category:
+------------+--------+
|  Category  | Amount |
+------------+--------+
|    Food    |  15.50 |
+------------+--------+


### 4. Save costs
- Select option **4** to save your expenses as a CSV file. You can specify a file name or press Enter to save the default file name with `expenses.csv`

Enter filename to save expenses (default 'expenses.csv'): expenses.csv
Expenses saved to expenses.csv

### 5. Weight cost
- Select option **5** to load previously saved costs from a CSV file. You can specify a file name or press Enter to load from the default `expenses.csv`.

Enter filename to load expenses (default 'expenses.csv'): expenses.csv
Expenses loaded from expenses.csv

### 6. Exit the application.
- Select option **6** to exit the application. The application ends with saying goodbye.

Exiting... Goodbye!

### File Structure
- expenses.csv: This file will store your recorded expenses (if saved).
- expense_tracker.py: The main Python script containing the application logic.
