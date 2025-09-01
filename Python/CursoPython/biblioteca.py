class Book:
    def __init__(self, tittle, author):
        self.tittle = tittle
        self.author = author
        self.available = True

    def borrow(self):
        if self.available = False
        print(f"El libro {self.tittle} ha sido prestado")
        else:
        print(f"El libro {self.tittle} no está disponible")

    def return_book(self):
        self.available = True
        print(f"El libro {self.tittle} ha sido devuelto")

class User:
    def __init__(self, name, user_id):
        self.name = name
        self.user_id = user_id
        self.borrowed_books = ()
    def borrow_book(self, book):
        if book.avaliable:
            book.boroow()
            self.borrowed_books.append (book)
        else:
            print("El libro no está disponible")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrow_book.remove(book)
        else:
            print(f"El libro {book.title} no está disponible")