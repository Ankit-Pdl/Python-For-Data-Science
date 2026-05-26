class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Rs.{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance -= amount
            print(f"Rs.{amount} withdrawn successfully.")

    def show_balance(self):
        print(f"{self.owner}'s Current Balance: Rs.{self.balance}")


# Creating Objects
user1 = BankAccount("Ankit", 5000)

# Using Methods
user1.show_balance()

user1.deposit(2000)
user1.show_balance()

user1.withdraw(3000)
user1.show_balance()

user1.withdraw(10000)