# Q9. Create a class BankAccount with:
# •	class variable bank_name
# •	instance variables holder and balance
# •	instance method deposit(amount)
# •	class method change_bank_name(cls, new_name)
# •	static method validate_amount(amount) → returns True if amount > 0
# Show transactions and how static + class methods work together

# class Bank:
#     Bank_name="cvbank"
#     def __init__(self,name,balance):
#         self.holder=name
#         self.balance=balance
#     @classmethod
#     def change_Bank_name(cls,union):
#         cls.Bank_name=union
#     def deposite(self,amount):
#         self.balance+=amount
#     @staticmethod
#     def validate(amount):
#         return amount>0
# b1=Bank("ravi",999999)
# b1.change_Bank_name("axis")
# b1.deposite(999999)
# print(b1.validate(898965))
# print(Bank.validate(b1.balance))

class student:
    def __init__ (self,name,marks):
        self.name=name
        self.marks=marks
    def is_passed(self):
        return self.marks>40
std1=student("man",55)
std2=student("can",35)

print(f'{std1.name} has {"passed" if std1.is_passed() else "failed"}')
print(f'{std2.name} has {"passed" if std2.is_passed() else "failed"}')
