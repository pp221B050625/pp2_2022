class BAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self):
        amount = int(input())
        self.balance += amount

    def withdraw(self):
        amount = int(input())
        if amount > self.balance:
            print("Withdrawal exceeds available balance")
        else:
            self.balance -= amount

a = BAccount("aldiar" , 10000)
a.deposit()
a.withdraw()
a.withdraw()