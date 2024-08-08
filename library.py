from datetime import *
from user import User

class Library():
    def __init__(self, name):
        self.name = name
        self.books = {}
        self.members = {}
        self.users = {}
        self.logged_in_user = None
    def add_new_books(self, book):
        if self.logged_in_user and self.logged_in_user.role == 'Librarian':
                     
            if book.isbn in self.books:
                print(f"The book with ISBN: {book.isbn} already exsists")
            else: 
                self.books[book.isbn] = book
                self.log_operation(f"Added book :{book.title}")
                print(f"The book: {book.title} has been added to the library")
        else: 
            print("Permission denied. Only librarians can add books.")
        
    def remove_book(self, isbn):
        if self.logged_in_user and self.logged_in_user.role == 'Librarian':
                     
            if isbn in self.books:
                removed_book = self.books.pop(isbn)
                print(f"Removed {removed_book.title} from the library")
                self.log_operation(f"Removed book:  {removed_book.title}")
            
            else: 
                print(f"No book with ISBN: {isbn} found.")

        else:
            print("Permission denied. Only librarians can add members.")
    def add_new_members(self, members):
        if self.logged_in_user and self.logged_in_user.role == 'Librarian':
            if members.member_id in self.members:
                print(f"Member with ID: {members.member_id} already exsists")
            else:
                self.members[members.member_id] = members
                print(f"The member named: {members.name} has joined the library")
                self.log_operation(f"Added member: {members.name}")
        else: 
            print("Permission denied. Only librarians can add members.")

    def remove_member(self, member_id):
        if self.logged_in_user and self.logged_in_user.role == 'Librarian':
            if member_id in self.members:
                removed_member = self.members.pop(member_id)
                self.log_operation(f"{self.members.name} has been removed")
                print(f"Removed member {removed_member.name} from the library")
            else:
                print(f"No member with ID {member_id} found")
        else: 
            print("Permission denied. Only librarians can remove members." )
    def search_books(self, title =None, author = None, isbn = None):
        results = []
        for book in self.books.values():
            if (title and title.lower() in book.title.lower()) or \
                (author and author.lower() in book.author.lower()) or \
                (isbn and isbn == book.isbn):
                results.append(book) 
                print("Test")
        return results
    
    def list_books(self):
        return self.books
        
    def check_out(self, isbn, member_id, checkout_days=14):
        for book in self.books:
            if book.isbn == isbn:
                print(f"The book {book.title} is already checkout by {book.checked_out_by}.")
                return
            else:
                book.checked_out_by = member_id
                book.due_date = datetime.now() + timedelta(days=checkout_days)
                self.get_member(member_id).borrowing_history.append(book.title)
                print(f"The book {book.title} has been checked out by {member_id}. Due date is {book.due_date}.")
                return
        print("Book not found")

    def return_book(self, isbn, member_id):
        for book in self.books:
            if book.isbn == isbn:
                if book.check_out_by == member_id:
                    book.check_out_book = None
                    book.due_date = None
                    print(f"The book {book.title} has been returned by {member_id}.")
                    if book.reservation_queue:
                        next_member_id = book.reservation_queue.pop(0)
                        print(f"Notication: The book {book.title} is now availble for membber{next_member_id}")
                        return
                else:
                    print(f"The book {book.title} has not been checkout out by this member id: {member_id}")
                    return
            print("Book not found")

    def reserve_book(self, isbn, member_id):
        for book in self.books:
            if book.isbn == isbn:
                if member_id not in book.reservation_queue:
                    book.reservation_queue.append(member_id)
                    print(f"The book {book.title} has been reserved by {member_id}")
                else:
                    print(f'The book {book.title} is already reserved by {member_id}.')
                return
        print("Book not found.")

    def check_overdue_books(self):
        overdue_books = []
        for book in self.books: 
            if book.checked_out_by and book.due_date < datetime.now():
                overdue_books.append(book)
            return overdue_books
        

    def filter_books_by_availability(self, available = True):
        return (book for book in self.books.values() if book.is_checked_out != available)
        
    def log_operation(self, operation):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = f"{timestamp} - {operation}\n"
        with open (f"{self.name}_log.txt", "a") as log_file:
            log_file.write(log_entry)  
    def add_user(self, username, password, role):
        if username in self.users:
            print(f"Username already exsists")
        else:
            self.users[username] = User(username, password, role)
            print(f'Added user {username} with role {role}')
            self.log_operation(f"Added user {username}")
    def remove_user(self, username):
        if username in self.users and self.logged_in_user == None:
            removed_user = self.users.pop(username)
            self.log_operation(f"{removed_user.username} has been removed")
            print(f"Removed member {removed_user.username} from the library")
        else:
            print(f"No member with user {username} found")
            
    def authenticate_user(self, username, password):
        if username in self.users and self.users[username].check_password(password):
            self.logged_in_user = self.users[username]
            print(f"User {username} authenticated. ")
            self.log_operation(f"Username: {username} has been authenticated. ")
        else:
            print("Authentication failed. Invalid username or password. ")
    def logout_user(self): 
        if self.logged_in_user:

            print(f"User {self.logged_in_user.username} logged out.")
            self.log_operation(f"User: {self.logged_in_user.username} has been logged out")
            
            self.logged_in_user = None
            
        else: 
            print("No user is logged in!")
    
    def get_member(self, member_id):
        for member in self.members:
            if member.member_id == member_id:
                return member
        return None

    
    def __str__(self):
        return f"Library name({self.name}, books = {[book.title for book in self.books.values()]}, members = {[member.name for member in self.members.values()]}, users{[user.username for user in self.users.values()]})"
    