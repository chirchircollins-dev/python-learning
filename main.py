expenses = []
def add_expense(name, amount):
    expense = {"name": name, "amount": amount}
    expenses.append(expense)
    print(f"✅✅Added {name} - ${amount}")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses now")
    else:
        print("\n Here is your expenses:")
        for expense in expenses:
            print(f"{expense["name"]} - ${expense["amount"]}")

def total_expenses():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print(f"Total spent is ${total}")
    

import json

def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file)
    print("✅ Expenses saved!")

def load_expenses():
    global expenses
    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)
    except FileNotFoundError:
        pass


def main():
    load_expenses()
    while True:
        print("\n Expense Tracker Menu 2")
        print("\n 1.Add your expense")
        print("\n 2.View your expenses")
        print("\n 3.My total expenses")
        print("\n 4.Quit")

        mychoice = input("Enter your choice:")

        if mychoice == "1":
            name = input("Enter Name:")
            amount = float(input("Enter amount:"))
            add_expense(name, amount)
        
        elif mychoice == "2":
            view_expenses()
        
        elif mychoice =="3":
            total_expenses()

        elif mychoice == "4":
            print("Bye,see you soon")
            save_expenses()
            break
        

        else:
            print("Invalid option")
            

main()
            
