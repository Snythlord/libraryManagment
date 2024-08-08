class Book:
    def __init__(self, title, author, isbn, genre, publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False
        self.genre = genre
        self.publication_year = publication_year
        self.reserved_by = None
        self.checked_out_by = None
        self.due_date = None
        self. reservation_queue = []
        

    #Turns true
    def check_out(self):
        self.is_checked_out = True

    def return_book(self):
        self.is_checked_out = False

    def reserve (self, member):
        self.reserved_by = member

    def __str__(self):
        Reservations = "Resservations: {len(self.reservation_queue)}" if self.reservation_queue else ""
        Status = f"Due date: {self.due_date}" if self.checked_out_by else "Availible"
        return (f"Book title {self.title}, Book Author {self.author}"
                f"genre = {self.genre}, publication year is = {self.publication_year}"
                f"is checked out = {self.is_checked_out}, reserved_by ={self.reserved_by}, Status: {Status}{Reservations}")
