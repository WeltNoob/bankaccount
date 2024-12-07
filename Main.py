class BankAccount:

    #constructor is used to initialize the account

    def init(self,account_holder,balance=0):

        self.account_holder = account_holder

        self.balance = balance

    def deposit(self,amount):

        if amount>=10:

            self.balance = self.balance + amount

            print(f"${amount} has been deposited.{self.account_holder}'s new balance is ${self.balance}")

    def withdraw(self,amount):

        if amount > 0 and amount <= self.balance:

            self.balance -= amount

            print(f"${amount} withdrawn. {self.account_holder}'s new balance is ${self.balance}")


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
    print(cred[user_name]["pin"])
    break
    pin_code = input("Type your pin code:\n")



print(cred[user_name]["pin"])