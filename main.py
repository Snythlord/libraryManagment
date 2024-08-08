from book import Book
from member import Member
from library import Library
from datetime import *

def main():
    # library = Library("Big Library")

    # book1 = Book("Harry Potter", "JK Rowling", 12345678, "Fiction", 2009)
    # book2 = Book("Lord of the Rings", "I forgot", 987651, "Fiction", 2008)
    # book3 = Book("Lord of the Rings 2", "I forgot", 90881, "Fiction", 2008)


    # library.add_new_books(book1)
    # library.add_new_books(book2)
    # library.add_new_books(book3)

    
    # member1 = Member("Bob", 713871, 6779499032)
    # member2 = Member("Joe", 81771, 6779492012)
    # member3 = Member("Staurt", 1933, 6779499012)


    # library.add_new_members(member1)
    # library.add_new_members(member2)
    # library.add_new_members(member3)

    # # case 1 

    # member1.check_out_book(book1)
    # member2.check_out_book(book2)
    # member1.check_out_book(book2)
    # member1.check_out_book(book3)

    # member3.check_out_book(book1)
    

    # member2.return_book(book2)

    # member1.check_out_book(book2)

    # # case 2 
    
    # member1.return_book(book1)

    # if (book1 in library.filter_books_by_availability()):
    #       print(f"This book is avaliable! at {datetime.now()}")
    #       member1.check_out_book(book1)
    # else:
    #     print(f"⚠︎ This book is unavailiable")
    
    # # It searches for 
    # for book_name in library.search_books("Lord of the Rings"):
    #     if (book_name in library.filter_books_by_availability()):
    #         print(f"{book_name.title} is avaliable at {datetime.now()}")
    #     else:
    #         print(f"{book_name.title} is unavailible!")
    
    # library.remove_member(member3.member_id)
    # member3.log_operation(f"{member3.name} has been removed from the library")

    # member1.return_book(book2)

    # def availibility_to_remove(book_to_be_removed):
    #     if book_to_be_removed.isbn in library.books:
    #         if book_to_be_removed.is_checked_out:
    #             print(f"{book_to_be_removed.title} is taken out and can not be removed")
    #         else:
    #              library.remove_book(book_to_be_removed.isbn)
    #              print(f"{book_to_be_removed.title} is removed at {datetime.now()}")
    #     else:
    #          print('There is an error')

    # availibility_to_remove(book2)
    # # x = int(input("Enter member ID: \n"))
    # x = 1
    # print(library.members )
    # print(x)
    # if library.members.get(x):
    #     # y = input("Do you want to remove your subsription? y/n \n")
    #     if y.lower() == "y":
    #          library.remove_member(x)
    #          library.log_operation(f"ID: {x} has been removed.")
    #     elif y.lower() == "n":
    #          print("Enjoy your time at the library. ")
    #     else: 
    #          print("That's not a valid option")
             
        
            
    # else:
    #      library.log_operation("Sorry you are not a part of this library.")
    
    # librarian1 = library.add_user("Joe", "password", "librarian")

    # library.authenticate_user("Joe", "password")

    

    # library.logout_user()

    # library.remove_user('Joe')

    # print(library.users.values())


    # print(library.__str__())
    # library.log_operation(f"{book2.title} has been removed")
    
    library1 = Library("The Library")

    book1 = Book("Charlies book 1", "Charlie", "123456789", "Biography", 1982)
    book2 = Book("Charlies book 2", "Charlie", "245679877", "Biography", 1982)
    book3 = Book("Charlies book 3", "Charlie", "999999999", "Biography", 1982)
    book4 = Book("Charlies book 4", "Charlie", "1", "Biography", 1982)
    book5 = Book("The Kindgom of Apes", "Kevin", "1234567809", "Biography", 1982)

    member1 = Member("Joe", 7582, any) #
    member2 = Member("Mohammed", "1", 5672)
    member3 = Member("Abdullah", 1222, 5672)
    member4 = Member("Rick", 1233, 5672)
    member5 = Member("Sam", 123, 5672)

    user1 = library1.add_user(56789, "password", "Librarian")
    user2 = library1.add_user(53489, "password", "Librarian")

    library1.authenticate_user(56789, "password")

    library1.add_new_books(book1)
    library1.add_new_books(book2)
    library1.add_new_books(book3)
    library1.add_new_books(book4)
    library1.add_new_books(book5)

    library1.add_new_members(member1)
    library1.add_new_members(member2)
    library1.add_new_members(member3)
    library1.add_new_members(member4)
    library1.add_new_members(member5)

    

    kevins_book = library1.search_books("1234567809")

    
if __name__ == "__main__":
        main()

        