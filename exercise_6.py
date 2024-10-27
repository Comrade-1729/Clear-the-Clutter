'''
    Library Management System
'''

class Library:
    ''' Library Class for library functions'''
    def __init__(self):
        #List to store all books in Library
        self.books = []

    def add_book(self, book_name):
        ''' Function to Add a new book to the Library '''
        self.books.append(book_name)
        print(f"'{book_name}' has been added to the Library.")

    def display_books(self):
        ''' Function to Display all available books '''
        if len(self.books) == 0:
            print("No books are available in the Library")
        else:
            print("\nAvailable Books in the Library : ")
            for i,book in enumerate(self.books):
                print(f"{i+1}. {book}")

    def issue_book(self,book_name):
        ''' Function to Issue a book to a user '''
        if book_name in self.books:
            self.books.remove(book_name)
            print(f"'{book_name}' has been issued from the Library.")
        else:
            print(f"Sorry, '{book_name}' is not available in the library.")

    def return_book(self, book_name):
        ''' Function to Return a book from a user '''
        self.books.append(book_name)
        print(f"'{book_name}' has been returned to the Library.")

class LibraryManagementSystem:
    ''' Class for the User Interface (to interact with the Library class) '''
    def __init__(self):
        self.library = Library()

    def run(self):
        ''' Function to display the Menu & to Handle use input '''
        while True:
            print("\nComrade's Library Management System")
            print("1. Display Available Books")
            print("2. Add a New Book")
            print("3. Issue a Book")
            print("4. Return a Book")
            print("5. Exit")
            choice = input("Enter your choice (1-5): ")

            # 'match, case is for python version 3.10 and later
            # match choice:
            #     case '1':
            #         self.library.display_books()
            #     case '2':
            #         book_name = input("Enter the name of the book to add : ")
            #         self.library.add_book(book_name)
            #     case '3':
            #         book_name = input("Enter the name of the book you want to Issue : ")
            #         self.library.issue_book(book_name)
            #     case '4':
            #         book_name = input("Enter the name of the book you want to return : ")
            #         self.library.issue_book(book_name)
            #     case '5':
            #         print("Thank you for using Comrade's Library Management System ;)")
            #         break
            #     case _:
            #         print("Invalid Choice! Please try again.")
            if choice == "1":
                self.library.display_books()
            elif choice == "2":
                book_name = input("Enter the name of the book to add: ")
                self.library.add_book(book_name)
            elif choice == "3":
                book_name = input("Enter the name of the book to issue: ")
                self.library.issue_book(book_name)
            elif choice == "4":
                book_name = input("Enter the name of the book to return: ")
                self.library.return_book(book_name)
            elif choice == "5":
                print("Thank you for using the Library Management System.")
                break
            else:
                print("Invalid choice. Please try again.")

#Create an instance of the LibraryManagementSystem and run it
library_system = LibraryManagementSystem()
library_system.run()
