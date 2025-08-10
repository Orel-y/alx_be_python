class BankAccount:
    def __init__(self, initial_balance=0):
        # Using an underscore to indicate it's intended for internal use (encapsulation)
        self._account_balance = float(initial_balance)

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self._account_balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if self._account_balance >= amount:
            self._account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        print(f"Current Balance: ${self._account_balance:.2f}")

