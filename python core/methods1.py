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

# class student:
#     def __init__ (self,name,marks):
#         self.name=name
#         self.marks=marks
#     def is_passed(self):
#         return self.marks>40
# std1=student("man",55)
# std2=student("can",35)
#
# print(f'{std1.name} has {"passed" if std1.is_passed() else "failed"}')
# print(f'{std2.name} has {"passed" if std2.is_passed() else "failed"}')


# class Car:
#     wheels = 4   # Class attribute shared by all cars
#
#     def __init__(self, mileage):
#         self.mileage = mileage   # Instance attribute
#
#     def display_specs(self):
#         print(f"Mileage: {self.mileage}, Wheels: {Car.wheels}")
#
#     @classmethod
#     def change_wheels(cls, new_wheels):
#         cls.wheels = new_wheels   # Updates class attribute
#
#
# # Create instances
# car1 = Car(15)
# car2 = Car(20)
#
# # Before changing wheels
# car1.display_specs()   # Mileage: 15, Wheels: 4
# car2.display_specs()   # Mileage: 20, Wheels: 4
#
# # Change wheels using class method
# Car.change_wheels(6)
#
# # After changing wheels
# car1.display_specs()   # Mileage: 15, Wheels: 6
# car2.display_specs()   # Mileage: 20, Wheels: 6



# class Temperature:
#     def __init__(self, celsius):
#         self.celsius = celsius   # Instance attribute
#
#     @staticmethod
#     def to_fahrenheit(celsius):
#         return (celsius * 9/5) + 32   # Static method
#
#     def show_conversion(self):
#         fahrenheit = Temperature.to_fahrenheit(self.celsius)
#         print(f"Celsius: {self.celsius}, Fahrenheit: {fahrenheit}")
#
#
# # Create instances
# t1 = Temperature(0)
# t2 = Temperature(25)
#
# # Show conversions
# t1.show_conversion()
# t2.show_conversion()
#
#
# class Book:
#     total_books = 0
#
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author
#         Book.total_books += 1
#
#     @classmethod
#     def from_string(cls, book_str):
#         title, author = book_str.split("-")
#         return cls(title, author)
#
#     @staticmethod
#     def is_valid_title(title):
#         return len(title) >= 3
#
#
# # Using constructor with validation
# if Book.is_valid_title("AI"):
#     b1 = Book("AI", "John")
# else:
#     print("Invalid title: AI")
#
# b2 = Book("Python", "Guido")
#
# # Using class method
# b3 = Book.from_string("DataScience-Jane")
#
# print(f"Total books: {Book.total_books}")
# print(b2.title, "-", b2.author)
# print(b3.title, "-", b3.author)


