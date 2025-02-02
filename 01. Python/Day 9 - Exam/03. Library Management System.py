class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def display_details(self):
        print()
        print("Book Title : ", self.title)
        print("Book Author : ", self.author)
        print("Book ISBN : ", self.isbn)

def main():
    book1 = Book("The Communist Manifesto", "Karl Marx", 987654321)
    book2 = Book("Harry Potter And The Goblet of Fire", "J.K. Rowling", 123456789)

    book1.display_details()
    book2.display_details()
main()