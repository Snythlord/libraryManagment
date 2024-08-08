from datetime import *

class Member:
    def __init__(self, name, member_id: int, contact_info):
        self.name = name
        self.member_id = member_id
        self.contact_info = contact_info
        self.checked_out_books = []
        self.reserved_books = []
        self.borrowing_history = []

    def check_out_book (self, book):
        if book.is_checked_out:
            print(f"⚠︎ {book.title} is already checked out.")
        else:
            book.check_out()
            self.checked_out_books.append(book)
            print(f"{self.name} now checked out {book.title}")
    def return_book(self, book):
        if book in self.checked_out_books:
            book.return_book()
            self.checked_out_books.remove(book)
            print(f"{self.name} has returned {book.title}")
            if book.reserved_by: 
                print(f"Book {book.title} is reserved by {book.reserved_by.name}")
                book.reserved_by.notify(f"{book.title} is now available")
        else:
            print(f"{self.name} does not have the book: {book.title} checked out.") 
    def log_operation(self, operation):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {operation}\n"
        with open (f"{self.name}_log.txt", "a") as log_file:
            log_file.write(log_entry) 
    def reserve_book(self, book):
        if book.is_checked_out and book.reserved_by is None:
            book.reserve()
            self.reserve_book.append(book)
            print(f"{self.name} reserved {book.title}")
        elif book.reserved_by:
            print(f"{book.title} is already reserved by {book.resereved_by.name}")
        else:
            print(f"{book.title} is available and does not need to be reserved. ")

    def notify(self, message):
        print(f"notification for {self.name}: {message}")
    def __str__(self):
        return (f"Member name: {self.name}, Member ID {self.member_id}, checked out books: {self.checked_out_books}"
                f"member info is {self.contact_info}")

