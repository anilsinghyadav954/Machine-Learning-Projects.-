"""
Bank Management System
-----------------------
A console-based banking application demonstrating:
- OOP (Bank, Account classes)
- File handling (accounts saved/loaded from a JSON file)
- Exception handling (custom exceptions for invalid operations)
- Functions (menu-driven operations)

Features:
1. Create new account
2. Deposit money
3. Withdraw money
4. Transfer money between accounts
5. View transaction history
6. View account details
7. List all accounts
8. Exit (auto-saves data)
"""

import json
import os
from datetime import datetime


DATA_FILE = "bank_data.json"


# ---------------------- Custom Exceptions ----------------------

class BankError(Exception):
    """Base exception for all bank-related errors."""
    pass


class AccountNotFoundError(BankError):
    """Raised when an account number does not exist."""
    pass


class InsufficientFundsError(BankError):
    """Raised when a withdrawal/transfer exceeds available balance."""
    pass


class InvalidAmountError(BankError):
    """Raised when a deposit/withdrawal amount is invalid (<= 0)."""
    pass


# ---------------------- Account Class ----------------------

class Account:
    def __init__(self, acc_no, name, balance=0.0, transactions=None):
        self.acc_no = acc_no
        self.name = name
        self.balance = balance
        self.transactions = transactions if transactions is not None else []

    def add_transaction(self, txn_type, amount, note=""):
        entry = {
            "type": txn_type,
            "amount": amount,
            "balance_after": self.balance,
            "note": note,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.transactions.append(entry)

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit amount must be greater than zero.")
        self.balance += amount
        self.add_transaction("DEPOSIT", amount)

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Withdrawal amount must be greater than zero.")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds. Available balance: {self.balance:.2f}"
            )
        self.balance -= amount
        self.add_transaction("WITHDRAW", amount)

    def to_dict(self):
        return {
            "acc_no": self.acc_no,
            "name": self.name,
            "balance": self.balance,
            "transactions": self.transactions,
        }

    @staticmethod
    def from_dict(data):
        return Account(
            data["acc_no"], data["name"], data["balance"], data["transactions"]
        )

    def __str__(self):
        return f"Account[{self.acc_no}] {self.name} - Balance: {self.balance:.2f}"


# ---------------------- Bank Class ----------------------

class Bank:
    def __init__(self, data_file=DATA_FILE):
        self.data_file = data_file
        self.accounts = {}
        self.next_acc_no = 1001
        self.load_data()

    # ---------- Persistence ----------

    def load_data(self):
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as f:
                    data = json.load(f)
                for acc_data in data.get("accounts", []):
                    acc = Account.from_dict(acc_data)
                    self.accounts[acc.acc_no] = acc
                self.next_acc_no = data.get("next_acc_no", 1001)
            except (json.JSONDecodeError, KeyError) as e:
                print(f"Warning: Could not fully load data file ({e}). Starting fresh.")

    def save_data(self):
        data = {
            "next_acc_no": self.next_acc_no,
            "accounts": [acc.to_dict() for acc in self.accounts.values()],
        }
        with open(self.data_file, "w") as f:
            json.dump(data, f, indent=4)

    # ---------- Core Operations ----------

    def create_account(self, name, initial_deposit=0.0):
        if initial_deposit < 0:
            raise InvalidAmountError("Initial deposit cannot be negative.")
        acc_no = self.next_acc_no
        account = Account(acc_no, name, 0.0)
        if initial_deposit > 0:
            account.deposit(initial_deposit)
        self.accounts[acc_no] = account
        self.next_acc_no += 1
        return account

    def get_account(self, acc_no):
        if acc_no not in self.accounts:
            raise AccountNotFoundError(f"Account {acc_no} not found.")
        return self.accounts[acc_no]

    def deposit(self, acc_no, amount):
        account = self.get_account(acc_no)
        account.deposit(amount)
        return account

    def withdraw(self, acc_no, amount):
        account = self.get_account(acc_no)
        account.withdraw(amount)
        return account

    def transfer(self, from_acc_no, to_acc_no, amount):
        if from_acc_no == to_acc_no:
            raise BankError("Cannot transfer to the same account.")
        from_acc = self.get_account(from_acc_no)
        to_acc = self.get_account(to_acc_no)

        # Withdraw first (raises if insufficient funds), then deposit
        from_acc.withdraw(amount)
        from_acc.add_transaction("TRANSFER_OUT", amount, note=f"To A/C {to_acc_no}")
        to_acc.deposit(amount)
        to_acc.add_transaction("TRANSFER_IN", amount, note=f"From A/C {from_acc_no}")
        return from_acc, to_acc

    def list_accounts(self):
        return list(self.accounts.values())


# ---------------------- Helper Input Functions ----------------------

def input_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")


def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid account number.")


# ---------------------- Menu Functions ----------------------

def menu_create_account(bank):
    name = input("Enter account holder name: ").strip()
    if not name:
        print("Name cannot be empty.")
        return
    initial = input_float("Enter initial deposit amount (0 for none): ")
    try:
        account = bank.create_account(name, initial)
        print(f"\nAccount created successfully!")
        print(f"Account Number: {account.acc_no}")
        print(f"Account Holder: {account.name}")
        print(f"Balance: {account.balance:.2f}")
    except BankError as e:
        print(f"Error: {e}")


def menu_deposit(bank):
    acc_no = input_int("Enter account number: ")
    amount = input_float("Enter deposit amount: ")
    try:
        account = bank.deposit(acc_no, amount)
        print(f"Deposit successful. New balance: {account.balance:.2f}")
    except BankError as e:
        print(f"Error: {e}")


def menu_withdraw(bank):
    acc_no = input_int("Enter account number: ")
    amount = input_float("Enter withdrawal amount: ")
    try:
        account = bank.withdraw(acc_no, amount)
        print(f"Withdrawal successful. New balance: {account.balance:.2f}")
    except BankError as e:
        print(f"Error: {e}")


def menu_transfer(bank):
    from_acc = input_int("Enter your account number: ")
    to_acc = input_int("Enter recipient account number: ")
    amount = input_float("Enter transfer amount: ")
    try:
        from_account, to_account = bank.transfer(from_acc, to_acc, amount)
        print("Transfer successful!")
        print(f"Your new balance: {from_account.balance:.2f}")
        print(f"Recipient ({to_account.name}) new balance: {to_account.balance:.2f}")
    except BankError as e:
        print(f"Error: {e}")


def menu_view_transactions(bank):
    acc_no = input_int("Enter account number: ")
    try:
        account = bank.get_account(acc_no)
        if not account.transactions:
            print("No transactions yet.")
            return
        print(f"\nTransaction History for {account.name} (A/C {acc_no})")
        print("-" * 70)
        for txn in account.transactions:
            print(
                f"{txn['timestamp']} | {txn['type']:<13} | "
                f"Amount: {txn['amount']:.2f} | "
                f"Balance After: {txn['balance_after']:.2f} | {txn['note']}"
            )
        print("-" * 70)
    except BankError as e:
        print(f"Error: {e}")


def menu_view_account(bank):
    acc_no = input_int("Enter account number: ")
    try:
        account = bank.get_account(acc_no)
        print("\nAccount Details")
        print("-" * 30)
        print(f"Account Number : {account.acc_no}")
        print(f"Account Holder : {account.name}")
        print(f"Balance        : {account.balance:.2f}")
        print(f"Total Txns     : {len(account.transactions)}")
        print("-" * 30)
    except BankError as e:
        print(f"Error: {e}")


def menu_list_accounts(bank):
    accounts = bank.list_accounts()
    if not accounts:
        print("No accounts found.")
        return
    print("\nAll Accounts")
    print("-" * 50)
    for acc in sorted(accounts, key=lambda a: a.acc_no):
        print(f"{acc.acc_no} | {acc.name:<20} | Balance: {acc.balance:.2f}")
    print("-" * 50)


# ---------------------- Main Program ----------------------

def show_menu():
    print("\n" + "=" * 40)
    print("       BANK MANAGEMENT SYSTEM")
    print("=" * 40)
    print("1. Create New Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Transfer Money")
    print("5. View Transaction History")
    print("6. View Account Details")
    print("7. List All Accounts")
    print("8. Exit")
    print("=" * 40)


def main():
    bank = Bank()
    actions = {
        "1": menu_create_account,
        "2": menu_deposit,
        "3": menu_withdraw,
        "4": menu_transfer,
        "5": menu_view_transactions,
        "6": menu_view_account,
        "7": menu_list_accounts,
    }

    while True:
        show_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "8":
            bank.save_data()
            print("Data saved. Thank you for using Bank Management System. Goodbye!")
            break
        elif choice in actions:
            try:
                actions[choice](bank)
            except Exception as e:
                # Catch-all safety net for unexpected errors
                print(f"Unexpected error: {e}")
            finally:
                bank.save_data()  # auto-save after every operation
        else:
            print("Invalid choice. Please select a number between 1 and 8.")


if __name__ == "__main__":
    main()