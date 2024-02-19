class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number=account_number
        self.__balance=balance

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance=balance
            return self.__balance
        else:
            print("Invalid Balance!")
    
    def deposit(self, amount):
        if amount > 0:
            self.__balance+=amount
        else:
            print("Invalid amount pls check!!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance-=amount
        else:
            print("Invalid withdrawal amount")

account=BankAccount(1234, 5000)
print(account._account_number, account.get_balance())

account.set_balance(30000)

account.deposit(450000)
print(account._account_number, account.get_balance())

account.withdraw(459)

print(account._account_number, account.get_balance())

