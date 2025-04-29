class Person:
    """To implement"""
    def __init__(self,first_name:str,last_name:str):
        self.first_name=first_name
        self.last_name=last_name
    def __str__(self):
        return f"{self.first_name},{self.last_name}"

    def _rep_(self):
        return f"Person({self.first_name},{self.last_name})"
    

        pass


class Book:
    """To implement"""
    def __init__(self,title:str,author:Person):
        self.title=title
        self.author=author
    def _rep_(self):
        return f"Book({self.title},{self.author})"
    def _str_(self):
        return f"{self.title},{self.author}"


class LibraryError(Exception):
    """Base class for Library errors"""
  


class Library:
    """To implement."""
    def _init_(self,name:str,_books:list[Book],_members:set[Person],_borrowed_books:dict[Book, Person]):
        self.name=name
        self._books=_books
        self._members=_members
        self._borrowed_books=_borrowed_books
    def _set_(self):
        return f"{self.name}"
    def is_book_available(self,book:Book):
        if book not in self._books:
            raise LibraryError('le livre n existe pas dans le catalogue de la bibliotheque')
    def borrow_book(self ,book: Book, person: Person):
        self._borrowed_books[book] = person
        print(f"{person} a emprunté le livre : {book}")
        if person not in self._members:
            raise LibraryError('a personne n est pas membre')
        if book not in self._books:
            raise LibraryError('le livre n existe pas dans le catalogue de la bibliotheque')
        if book in self._borrowed_books:
            raise LibraryError('le livre est deja emprunte')
    def return_book(self,book: Book):
        if book in self._borrowed_books:
             print(f"{person} a emprunté le livre : {book}")
        else:
            raise LibraryError('le livre n est pas emprunte')
    def add_new_member(self,person:Person):
        self._members.add(person)
    def add_new_book(self,book: Book):
        self._books.add(book)
    def print_status(self):
        print(f"{self.name} status:")
        print(f"Books catalogue: {self._books}")
        print(f"Members: {self._members}")
        available_books = [book for book in self._books if book not in self._borrowed_books]
        print(f"Available books: { available_books}")

        print(f"Borrowed books: {self._borrowed_books}")

    
        


def main():
    """Test your code here"""
antoine = Person("Antoine", "Dupont")
print(antoine)

julia = Person("Julia", "Roberts")
print(julia)

rugby_book = Book("Jouer au rugby pour les nuls", Person("Louis", "BB"))
print(rugby_book)

novel_book = Book("Vingt mille lieues sous les mers", Person("Jules", "Verne"))
print(novel_book)



library.add_new_book(rugby_book)
library.add_new_book(novel_book)
library.add_new_member(antoine)
library.add_new_member(julia)
library.print_status()

print(f"Is {rugby_book} available? {library.is_book_available(rugby_book)}")
library.borrow_book(rugby_book, antoine)
library.print_status()

try:
    library.borrow_book(rugby_book, julia)
except LibraryError as error:
    print(error)

try:
    library.borrow_book(Book("Roméo et Juliette", Person("William", "Shakespeare")), julia)
except LibraryError as error:
    print(error)

try:
    library.borrow_book(novel_book, Person("Simone", "Veil"))
except LibraryError as error:
    print(error)

try:
    library.return_book(novel_book)
except LibraryError as error:
    print(error)

library.return_book(rugby_book)
library.borrow_book(novel_book, julia)
library.print_status()

library.borrow_book(rugby_book, julia)
library.print_status()

if __name__ == "__main__":
    main()
