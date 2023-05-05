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

def main():
   print("Hello from main!")

if __name__ == "__main__":
   main()