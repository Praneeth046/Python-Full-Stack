class Book:
    total_books=0
    def __init__ (self,title,author):
        self.title=title
        self.author=author
        Book.total_books+=1
    def from_string(cls, book_str):
        title, author = book_str.split("-")
        cls(title,author)
b1 = Book("Python", "ram")
b2 = Book("java","sai")
print(f"Total books: {Book.total_books}")
print(b1.title, "-", b1.author)
print(b2.title, "-", b2.author)