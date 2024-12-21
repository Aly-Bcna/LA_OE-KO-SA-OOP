OE#06

class BankAccount:
    def __init__(self, account_number, balance):
        self.__account_number = account_number
        self.__balance = balance
   
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
          print("Invalid deposit amount.")
       
    def withdraw(self, amount):
        if amount > 0 and amount <=self.__balance:
            self.__balance -= amount
        else:
         print("Amount must be positive and less than or equal to the current balance.")
       
    def display_account_info(self):
         print(f"Account Number: {self.__account_number}")
         print(f"Current Balance: {self.__balance}")
         
    def get_account_number(self):
        return self.__account_number
    def get_balance(self):
        self.display_balance()
    def set_balance(self, balance):
        if balance >= 0:
            self.__balance = balance
        else:
            print("Invalid balance. Balance must be non-negative.")
         
    def display_balance(self):
        print(f"Current Balance: {self.__balance}")
           
pera = BankAccount(1235, 3000.00)
pera.display_account_info()
pera.deposit(float(input("Add Amount: ")))
pera.display_account_info()
pera.withdraw(float(input("Deduct Amount: ")))
pera.display_account_info()
pera.set_balance(float(input("Set Balance: ")))
pera.display_account_info()
       
