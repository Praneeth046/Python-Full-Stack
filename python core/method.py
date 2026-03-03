# Q9. Create a class BankAccount with:
# •	class variable bank_name
# •	instance variables holder and balance
# •	instance method deposit(amount)
# •	class method change_bank_name(cls, new_name)
# •	static method validate_amount(amount) → returns True if amount > 0
# Show transactions and how static + class methods work together

class Bank:
    Bank_name="cvbank"
    def __init__(self,name,balance):
        self.holder=name
        self.balance=balance
    @classmethod
    def change_Bank_name(cls,union):
        cls.Bank_name=union
    def deposite(self,amount):
        self.balance+=amount
    @staticmethod
    def validate(amount):
        return amount>0
b1=Bank("ravi",999999)
b1.change_Bank_name("axis")
b1.deposite(999999)
print(b1.validate(898965))
print(Bank.validate(b1.balance))

