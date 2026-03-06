##1
# l =[[1, 2], [3, 4], [5, 6]]
# z =list(map(lambda l:l +[5],l))
# print(z)

##2
# d = {"apple": 100, "banana": 40, "cherry": 150}
# k=dict(filter(lambda x: x[1]>50,d.items()))
# print(k)
# print(d.keys())
# print(d.items())
# print(d.values())

##3
from functools import reduce
# s=[1,5,8,6,3]
# r=reduce(lambda x,y:x if x>y else y,s)
# print(r)

##5
# s=("varma")
# z=list(map(lambda x:ord(x),s))
# print(z)

##6
# v = "AEIOUaeiou"
# t = list(filter(lambda x: x not in v,input()))
# print(t)

##7

# s= ['P', 'y', 't', 'h', 'o', 'n']
# r=reduce(lambda x,y:x+y,s)
# print(r)

##8
# s=[10, 350, 10, 350, 20]
# r=list(map(lambda x:id(x),s))
# print(r)

##10

# s=[5, 10, 15, 20, 25, 30]
# r=reduce(lambda a,b:a+b,filter(lambda x:x%5==0,map(lambda x:x**2,s)))
# print(r)



##2
# a= [1, 2, 3, 4]
# b = [10, 20, 30, 40]
# k=list(map(lambda x,y:x+y,a,b))
# print(k)


##3
# n = [12, 15, 7, 18, 20, 21, 25]
# k=list(filter(lambda x: (x%3==0) ^ (x%5==0),n))
# print(k)


##4
# n = [1, 2, 3, 4]
# k=reduce(lambda a,b:a+b,n,10)
# print(k)


##5
# nums = [[1, 2], [3, 4], [5, 6]]
# result = list(map(lambda x: x.append(10), nums))
# print("Result:", nums)
# print("Nums:", nums)
class Book:
    total_books = 0   # Class variable

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.total_books += 1

    @classmethod
    def from_string(cls, book_str):
        title, author = book_str.split("-")
        return cls(title, author)

    @staticmethod
    def is_valid_title(title):
        return len(title) >= 3


# Using constructor
if Book.is_valid_title("AI"):
    b1 = Book("AI", "John")
else:
    print("Invalid title: AI")

b2 = Book("Python", "Guido")

# Using class method
b3 = Book.from_string("DataScience-Jane")

print(f"Total books: {Book.total_books}")
print(b2.title, "-", b2.author)
print(b3.title, "-", b3.author)
