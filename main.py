import sys
class Book:
    def __init__(self, title, author, publication_year, ISBN):
        self.title = title
        self.author = author
        self.publication_year = publication_year
        self.ISBN = ISBN
        self.checked_out_by = None

    def __repr__(self):
        return f"{self.title} by {self.author} ({self.publication_year})"

    def checkout(self, patron):
        if self.checked_out_by is None:
            self.checked_out_by = patron
            return True
        else:
            return False

    def checkin(self):
        if self.checked_out_by is not None:
            self.checked_out_by = None
            return True
        else:
            return False
        
class Patron:
    def __init__(self, name):
        self.name = name
        self.checked_out_books = []

    def __repr__(self):
        return self.name

    def checkout(self, book):
        if book.checkout(self):
            self.checked_out_books.append(book)
            return True
        else:
            return False
   
    def checkin(self, book):
        if book.checkin():
            self.checked_out_books.remove(book)
            return True
        else:
            return False

class Library:
    def __init__(self, books, patrons):
        self.books = books
        self.patrons = patrons

    def display_books(self):
        for book in self.books:
            if book.checked_out_by is None:
                print(book)

    def display_patrons(self):
        for patron in self.patrons:
            print(patron)

    def search_books(self, search_string):
        matching_books = []
        for book in self.books:
            if search_string.lower() in book.title.lower() or search_string.lower() in book.author.lower():
                matching_books.append(book)
        return matching_books
    
    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def find_patron(self, name):
        for patron in self.patrons:
            if patron.name == name:
                return patron
        return None


def main():
    # Create some books and patrons
    book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, "978-0-7432-7356-5")
    book2 = Book("To Kill a Mockingbird", "Harper Lee", 1960, "0-446-31078-6")
    book3 = Book("Pride and Prejudice", "Jane Austen", 1813, "978-0-14-143951-8")
    patron1 = Patron("Alice")
    patron2 = Patron("Bob")
    
    # Create the library and add the books and patrons to it
    library = Library([book1, book2, book3], [patron1, patron2])

    # Parse command line arguments
    if len(sys.argv) != 3:
        print("Usage: python main.py <patron name> <book title>")
        print("Use \"quotations\" for patron name and book title!")
        return
    
    patron_name = sys.argv[1]
    book_title = sys.argv[2]

    # Find the patron and book objects in the library
    patron = library.find_patron(patron_name)
    book = library.find_book(book_title)

    # Rent the book to the patron
    if patron.checkout(book):
        print(f"{book_title} checked out by {patron_name}")
    else:
        print(f"{book_title} is already checked out")

if __name__ == "__main__":
   main()