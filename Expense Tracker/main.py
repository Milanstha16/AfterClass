import json
import csv
import os
from datetime import datetime


# ---------------- Folder & File Setup ---------------- #

# Get the folder where main.py is located
BASE_FOLDER = os.path.dirname(os.path.abspath(__file__))

# Store files in the same folder as main.py
FILE_NAME = os.path.join(BASE_FOLDER, "expenses.json")
CSV_FILE = os.path.join(BASE_FOLDER, "expenses.csv")
BUDGET_FILE = os.path.join(BASE_FOLDER, "budget.json")


# ---------------- File Handling ---------------- #

def load_data(filename):
    if os.path.exists(filename):
        try:
            with open(filename, "r") as file:
                return json.load(file)
        except:
            return {}
    return {}


def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


# ---------------- Expense Functions ---------------- #

def add_expense(expenses):

    print("\nAdd New Expense")

    date = input("Enter date (YYYY-MM-DD): ")

    try:
        datetime.strptime(date, "%Y-%m-%d")
    except:
        print("Invalid date format.")
        return


    category = input("Enter category: ")


    while True:

        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("Amount must be positive.")
                continue

            break

        except:
            print("Enter a valid number.")


    description = input("Enter description: ")


    expense = {
        "date": date,
        "category": category,
        "amount": amount,
        "description": description
    }


    expenses.append(expense)

    save_data(FILE_NAME, expenses)

    check_budget(expenses)

    print("Expense added successfully.\n")



def view_expenses(expenses):

    if not expenses:
        print("No expenses found.\n")
        return


    print("\n========== Expenses ==========")


    for index, expense in enumerate(expenses, 1):

        print(f"""
Expense {index}
Date        : {expense['date']}
Category    : {expense['category']}
Amount      : ${expense['amount']:.2f}
Description : {expense['description']}
-------------------------------
""")



def search_category(expenses):

    category = input("Enter category: ").lower()

    found = False


    for expense in expenses:

        if expense["category"].lower() == category:

            found = True

            print(expense)


    if not found:
        print("No expense found.")



def total_spending(expenses):

    total = sum(e["amount"] for e in expenses)

    print(f"Total Spending: ${total:.2f}")



# ---------------- Bonus Features ---------------- #

def monthly_summary(expenses):

    month = input("Enter month (YYYY-MM): ")

    total = 0


    for expense in expenses:

        if expense["date"].startswith(month):

            total += expense["amount"]


    print(f"Total spending for {month}: ${total:.2f}")



def highest_lowest(expenses):

    if not expenses:

        print("No data available.")
        return


    highest = max(expenses, key=lambda x:x["amount"])

    lowest = min(expenses, key=lambda x:x["amount"])


    print("\nHighest Expense")

    print(highest)


    print("\nLowest Expense")

    print(lowest)



def category_summary(expenses):

    summary = {}


    for expense in expenses:

        category = expense["category"]

        summary[category] = summary.get(category,0) + expense["amount"]



    print("\nCategory Summary")


    for category, amount in summary.items():

        print(f"{category}: ${amount:.2f}")




def filter_by_date(expenses):

    start = input("Enter start date YYYY-MM-DD: ")

    end = input("Enter end date YYYY-MM-DD: ")


    print("\nFiltered Expenses")


    for expense in expenses:

        if start <= expense["date"] <= end:

            print(expense)




def set_budget():

    while True:

        try:

            budget = float(input("Enter monthly budget: "))

            break


        except:

            print("Invalid amount.")


    save_data(BUDGET_FILE, {"budget":budget})

    print("Budget saved.")




def check_budget(expenses):

    budget_data = load_data(BUDGET_FILE)


    if "budget" not in budget_data:

        return


    budget = budget_data["budget"]


    current_month = datetime.now().strftime("%Y-%m")


    spent = sum(
        e["amount"]
        for e in expenses
        if e["date"].startswith(current_month)
    )



    if spent > budget:

        print("\n⚠ WARNING: Budget exceeded!")


    elif spent >= budget * 0.8:

        print("\n⚠ You have used 80% of your budget.")




def edit_expense(expenses):

    view_expenses(expenses)


    try:

        index = int(input("Enter expense number to edit: ")) - 1


        if index < 0 or index >= len(expenses):

            print("Invalid selection.")

            return


        expense = expenses[index]


        expense["category"] = input("New category: ")

        expense["description"] = input("New description: ")

        expense["amount"] = float(input("New amount: "))


        save_data(FILE_NAME, expenses)


        print("Expense updated.")


    except:

        print("Invalid input.")




def delete_expense(expenses):

    view_expenses(expenses)


    try:

        index = int(input("Enter expense number to delete: ")) - 1


        expenses.pop(index)


        save_data(FILE_NAME, expenses)


        print("Expense deleted.")


    except:

        print("Invalid selection.")




def export_csv(expenses):

    with open(CSV_FILE,"w",newline="") as file:


        writer = csv.DictWriter(
            file,
            fieldnames=[
                "date",
                "category",
                "amount",
                "description"
            ]
        )


        writer.writeheader()

        writer.writerows(expenses)


    print("Exported to CSV successfully.")




# ---------------- Main Program ---------------- #

def main():

    expenses = load_data(FILE_NAME)


    if not isinstance(expenses,list):

        expenses=[]



    while True:


        print("""
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

""")


        choice = input("Choose option: ")



        if choice == "1":

            add_expense(expenses)


        elif choice == "2":

            view_expenses(expenses)


        elif choice == "3":

            search_category(expenses)


        elif choice == "4":

            total_spending(expenses)


        elif choice == "5":

            monthly_summary(expenses)


        elif choice == "6":

            highest_lowest(expenses)


        elif choice == "7":

            category_summary(expenses)


        elif choice == "8":

            filter_by_date(expenses)


        elif choice == "9":

            set_budget()


        elif choice == "10":

            edit_expense(expenses)


        elif choice == "11":

            delete_expense(expenses)


        elif choice == "12":

            export_csv(expenses)


        elif choice == "13":

            save_data(FILE_NAME, expenses)

            print("Goodbye!")

            break


        else:

            print("Invalid option.")




if __name__ == "__main__":

    main()