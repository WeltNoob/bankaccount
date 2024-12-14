class BankAccount:

    #constructor is used to initialize the account

    def __init__(self,account_holder,balance=0):

        self.account_holder = account_holder

        self.balance = balance

    def deposit(self,amount):

        if amount>=10:

            self.balance = self.balance + amount

            print(f"\n${amount} has been deposited. {self.account_holder.capitalize()}'s new balance is ${self.balance}\n")

    def withdraw(self,amount):

        if amount > 0 and amount <= self.balance:

            self.balance -= amount

            print(f"\n${amount} withdrawn. {self.account_holder.capitalize()}'s new balance is ${self.balance}\n")


cred = {
    "alice":{"pin":1000},
    "bob":{"pin":1001},
    "john":{"pin":1002},
    "sam":{"pin":1003}
}

while True:
    user_name = input("Type your username:\n")
    if user_name not in cred:
        print("Username was not found. Try again")
        continue
    pin_code = int(input("Type your pin code:\n"))
    if pin_code != cred[user_name]["pin"]:
        print("Pin code is not found. Try again!")
        continue
    break

user_name = BankAccount(user_name)
print("Welcome,",user_name )

while True:
    print(" 1. Deposit")
    print(" 2. Wtihdraw")
    print(" 3. Check balance")
    print(" 4. Exit")
    ans = input()

    if ans == "1":
        amount = int(input("How much will you deposit?:\n"))
        user_name.deposit(amount)
    elif ans == "2":
        amount = int(input("How much will you withdraw?:\n"))
        user_name.withdraw(amount)
    elif ans == "3":
        print(f"\n{user_name.account_holder}: ${user_name.balance}\n")
    elif ans == "4":
        break


