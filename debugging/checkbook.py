class Checkbook:
    def __init__(self):
        self.balance = 0.0

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return
        self.balance += amount
        print(f"Deposited ${amount:.2f}")
        self.print_balance()

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
            return
        self.balance -= amount
        print(f"Withdrew ${amount:.2f}")
        self.print_balance()

    def print_balance(self):
        print(f"Current Balance: ${self.balance:.2f}")

    def get_balance(self):
        return self.balance
