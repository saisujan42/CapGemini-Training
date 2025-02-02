class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __add__(self, book2):
        return Book(f"{self.title} & {book2.title}", self.author)
    
    def display(self):
        print("Title : ", self.title)
        print("Author : ", self.author)

def main():
    book1 = Book("Harry Potter", "J.K. Rowling")
    book2 = Book("Fantastic Beasts", "J.K. Rowling")

    books = book1 + book2
    books.display()
main()