# Expense Tracker

A simple Python-based Expense Tracker application that helps users record, manage, and analyze their daily expenses. The application allows users to add expenses, view records, search expenses, track spending, set budgets, and generate reports.

## Features

### Core Features
- Add new expenses
- View all recorded expenses
- Search expenses by category
- Calculate total spending
- Save expenses permanently using JSON files

### Expense Information Stored
Each expense contains:
- Date
- Category
- Amount
- Description

### Bonus Features
- Monthly expense summary
- Highest expense tracking
- Lowest expense tracking
- Category-wise spending summary
- Budget limit with warning messages
- Filter expenses by date range
- Edit existing expenses
- Delete expenses
- Export expenses to CSV format

---

## Project Structure

```
Expense Tracker
│
├── main.py
├── expenses.json
├── budget.json
├── expenses.csv
└── README.md
```

### File Description

| File | Purpose |
|------|---------|
| `main.py` | Main Python application |
| `expenses.json` | Stores all expense records |
| `budget.json` | Stores user budget information |
| `expenses.csv` | Exported expense report |
| `README.md` | Project documentation |

---

## Technologies Used

- Python 3
- JSON File Handling
- CSV File Handling
- datetime Module

---

## Python Concepts Practiced

This project demonstrates:

- Variables
- Lists
- Dictionaries
- Functions
- Loops
- Conditional Statements
- File Handling
- Exception Handling
- Data Validation

---

## Installation and Setup

### 1. Download or Clone the Project

Place the project folder in your desired location.

Example:

```
AfterClass
│
└── Expense Tracker
    │
    └── main.py
```

---

### 2. Run the Program

Open the terminal inside the **Expense Tracker** folder.

Run:

```bash
python main.py
```

---

## How to Use

When the program starts, you will see:

```
========== Expense Tracker ==========

1. Add Expense
2. View Expenses
3. Search by Category
4. Total Spending
5. Monthly Summary
6. Highest & Lowest Expense
7. Category-wise Spending
8. Filter by Date
9. Set Budget
10. Edit Expense
11. Delete Expense
12. Export CSV
13. Exit
```

Choose an option by entering the menu number.

---

## Example Expense

```
Date        : 2026-07-24
Category    : Food
Amount      : $25.50
Description : Lunch with friends
```

The data will automatically be saved in:

```
expenses.json
```

---

## Budget System

Users can set a monthly budget.

The application will display warnings when:

- Spending reaches 80% of the budget
- Spending exceeds the budget limit

Example:

```
⚠ You have used 80% of your budget.

```

or

```
⚠ WARNING: Budget exceeded!
```

---

## Exporting Data

Users can export expense records into CSV format.

The generated file:

```
expenses.csv
```

can be opened using:
- Microsoft Excel
- Google Sheets
- Other spreadsheet applications

---

## Error Handling

The application handles common errors such as:

- Invalid amount input
- Incorrect date format
- Invalid menu selection
- Missing data files

---

## Future Improvements

Possible upgrades:

- Add a graphical user interface using Tkinter
- Add user accounts and authentication
- Use SQLite database instead of JSON storage
- Add expense charts and graphs using Matplotlib
- Create a mobile version
- Add cloud backup support

---

## Author

Created as a Python programming project for practicing programming fundamentals and file handling.

---

## License

This project is free to use for learning and educational purposes.