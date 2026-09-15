# ==========================================
# PERSONAL EXPENSE TRACKER
# ==========================================

FILE_NAME = "expenses.txt"


# ------------------------------------------
# 1. Add Expense
# ------------------------------------------
def add_expense():
    print("\n---------- Add Expense ----------")

    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{category},{amount},{description}\n")

    print("Expense added successfully!")


# ------------------------------------------
# 2. Read Expenses from File
# ------------------------------------------
def get_expenses():
    expenses = []

    try:
        with open(FILE_NAME, "r") as file:
            for line in file:
                data = line.strip().split(",")

                if len(data) == 4:
                    expense = {
                        "date": data[0],
                        "category": data[1],
                        "amount": float(data[2]),
                        "description": data[3]
                    }

                    expenses.append(expense)

    except FileNotFoundError:
        pass

    return expenses


# ------------------------------------------
# 3. Show All Expenses
# ------------------------------------------
def show_expenses():
    expenses = get_expenses()

    print("\n---------- All Expenses ----------")

    if len(expenses) == 0:
        print("No expenses found.")
        return

    print("-" * 75)
    print(f"{'Date':<15}{'Category':<15}{'Amount':<15}{'Description'}")
    print("-" * 75)

    for expense in expenses:
        print(
            f"{expense['date']:<15}"
            f"{expense['category']:<15}"
            f"₹{expense['amount']:<14.2f}"
            f"{expense['description']}"
        )

    print("-" * 75)


# ------------------------------------------
# 4. Calculate Total Spending
# ------------------------------------------
def total_spending():
    expenses = get_expenses()

    total = 0

    for expense in expenses:
        total += expense["amount"]

    print("\n---------- Total Spending ----------")
    print(f"Total spending: ₹{total:.2f}")


# ------------------------------------------
# 5. Category-wise Spending
# ------------------------------------------
def category_wise_spending():
    expenses = get_expenses()

    category_total = {}

    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]

        if category in category_total:
            category_total[category] += amount
        else:
            category_total[category] = amount

    print("\n---------- Category-wise Spending ----------")

    if len(category_total) == 0:
        print("No expenses found.")
        return

    for category, total in category_total.items():
        print(f"{category}: ₹{total:.2f}")


# ------------------------------------------
# 6. Monthly Spending
# ------------------------------------------
def monthly_spending():
    expenses = get_expenses()

    month = input("\nEnter month (MM-YYYY): ")

    total = 0

    for expense in expenses:
        # Extract MM-YYYY from DD-MM-YYYY
        expense_month = expense["date"][3:]

        if expense_month == month:
            total += expense["amount"]

    print("\n---------- Monthly Spending ----------")
    print(f"Spending for {month}: ₹{total:.2f}")


# ------------------------------------------
# 7. Search by Category
# ------------------------------------------
def search_category():
    expenses = get_expenses()

    category = input("\nEnter category to search: ")

    found = False
    total = 0

    print("\n---------- Category Expenses ----------")

    for expense in expenses:

        if expense["category"].lower() == category.lower():

            print(
                f"{expense['date']} | "
                f"₹{expense['amount']:.2f} | "
                f"{expense['description']}"
            )

            total += expense["amount"]
            found = True

    if found:
        print(f"\nTotal spent on {category}: ₹{total:.2f}")
    else:
        print("No expenses found in this category.")


# ------------------------------------------
# 8. Main Menu
# ------------------------------------------
def main():

    while True:

        print("\n")
        print("=" * 45)
        print("       PERSONAL EXPENSE TRACKER")
        print("=" * 45)

        print("1. Add Expense")
        print("2. Show All Expenses")
        print("3. Total Spending")
        print("4. Category-wise Spending")
        print("5. Monthly Spending")
        print("6. Search by Category")
        print("7. Exit")

        print("=" * 45)

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            show_expenses()

        elif choice == "3":
            total_spending()

        elif choice == "4":
            category_wise_spending()

        elif choice == "5":
            monthly_spending()

        elif choice == "6":
            search_category()

        elif choice == "7":
            print("\nThank you for using Personal Expense Tracker!")
            break

        else:
            print("\nInvalid choice! Please try again.")


# ------------------------------------------
# Program Starts Here
# ------------------------------------------
if __name__ == "__main__":
    main()