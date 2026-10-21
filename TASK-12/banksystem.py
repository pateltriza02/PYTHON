class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def show_balance(self):
        print("Balance:", self.balance)


class SavingsAccount(BankAccount):
    def interest(self):
        print("Savings Account Interest: 4%")


class CurrentAccount(BankAccount):
    def account_type(self):
        print("This is Current Account")


s = SavingsAccount(10000)
s.show_balance()
s.interest()

c = CurrentAccount(20000)
c.show_balance()
c.account_type()