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

def main():
   print("Hello from main!")

if __name__ == "__main__":
   main()