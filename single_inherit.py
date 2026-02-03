class Book:
    def __init__(self,title,author):
        self.title=title
        self.author=author
    def display_book_details(self):
        print("Book Details:")
        print("Title:",self.title)
        print("Author:",self.author)
class IssuedBook(Book):
    def __init__(self,title,author,issued_to,issued_date):
        super().__init__(title,author)
        self.issued_to=issued_to
        self.issued_date=issued_date
    def display_issued_book_details(self):
        print("ISSUED BOOK DETAILS")
        super().display_book_details()
        print("Issued to:",self.issued_to)
        print("Issued date:",self.issued_date)
book1=IssuedBook("Python Programming","guido van rossum","Supritha","03-02-2026")
book1.display_issued_book_details()