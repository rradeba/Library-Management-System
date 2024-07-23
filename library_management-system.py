import sys

# Global variables and imports
library_dictionary = {
    'Book': ["Cat and the Hat", "Lifespan", "Huckleberry Fin"],
    'User': {'User Name': ["John", "Dave", "Steve"], 'User phone': ["11111111", "222222222", "333333333"], 'User Standing': ["Good", "Good", "Books Out"]},
    'Author': ["Dr. Suess", "David Sinclair", "Mark Twain"],
    'Genre': ["Fiction", "Non-Fiction", "Fiction"],
    'Book Status': ["Out", "Avaialble", "Out"]
}

library_genre = {
    'Fiction': 'Genre based on imaginary events.',
    'Non-Fiction': 'Genre based on real events.',
    'Fantasy': 'Genre based on imagined, improbable events.',
    'Mystery': 'Genre based on puzzling events.',
    'Humor': 'Genre intended to be funny.',
    'Poetry': 'Genre intended to communicate feelings.'
}

# Class for Book
class Book:  
    def __init__(self, library_dictionary):
        self.library_dictionary = library_dictionary
    
    def add_book(self):
        while True:  
            try:
                new_book = input("Add book title: ")
                self.library_dictionary["Book"].append(new_book)
                new_author = input("Add book author: ")
                self.library_dictionary["Author"].append(new_author)
                new_genre = input("Add book genre: ")
                self.library_dictionary["Genre"].append(new_genre)
                self.library_dictionary["Book Status"].append("Available")
                print("Book added.")
                break
            except TypeError:
                print("Please type a book name.")
    
    def borrow_book(self): 
        print("Books:")
        for book_index, book in enumerate(self.library_dictionary["Book"]):
            print(f"{book_index}: {book}")
        while True:  
            try:
                book_index = int(input("Type book index to borrow: "))
                if 0 <= book_index < len(self.library_dictionary["Book"]):
                    self.library_dictionary["Book Status"][book_index] = "Out"
                    print(f"{self.library_dictionary['Book'][book_index]} has been checked out.")
                    break
                else:
                    print("Invalid index. Please try again.")
            except (TypeError, ValueError):
                print("Please type a valid index.")
    
    def return_book(self): 
        print("Books:")
        for book_index, book in enumerate(self.library_dictionary["Book"]):
            print(f"{book_index}: {book}")
        while True:  
            try:
                book_index = int(input("Type book index to return: "))
                if 0 <= book_index < len(self.library_dictionary["Book"]):
                    self.library_dictionary["Book Status"][book_index] = "Available"
                    print(f"{self.library_dictionary['Book'][book_index]} has been checked back in.")
                    break
                else:
                    print("Invalid index. Please try again.")
            except (TypeError, ValueError):
                print("Please type a valid index.")

    def search_book(self): 
        search_book = input("Search title: ")
        for book_index, book in enumerate(self.library_dictionary["Book"]):
            if book == search_book: 
                print(f"------------------------\nTitle: {self.library_dictionary['Book'][book_index]}\nAuthor: {self.library_dictionary['Author'][book_index]}\nGenre: {self.library_dictionary['Genre'][book_index]}\nBook Status: {self.library_dictionary['Book Status'][book_index]}\n------------------------")
                return
        print("Book not found.")

    def book_menu(self):
        while True:  
            book_menu_selection = input("-----------------------------------\n 1. Add a new book\n 2. Borrow a Book\n 3. Return a Book\n 4. Search for a Book\n 5. Quit\n------------------------------------\n")
            if book_menu_selection == "1":
                self.add_book()
            elif book_menu_selection == "2":
                self.borrow_book()
            elif book_menu_selection == "3":
                self.return_book()
            elif book_menu_selection == "4":
                self.search_book()
            elif book_menu_selection == "5":
                break
            else:
                print("Invalid selection. Please try again.")

# Class for User
class User:
    def __init__(self, library_dictionary):
        self.library_dictionary = library_dictionary
    
    def add_user(self):
        while True:  
            try:
                new_user_name = input("User name: ")
                self.library_dictionary["User"]["User Name"].append(new_user_name)
                new_user_phone = input("User phone number: ")
                self.library_dictionary["User"]["User phone"].append(new_user_phone)
                self.library_dictionary["User"]["User Standing"].append("Good")
                print("User added.")
                break
            except TypeError:
                print("Please type value correctly.")
    
    def view_user(self):
        search_user_name = input("Type User name to view information: ")
        for user_index, user in enumerate(self.library_dictionary["User"]["User Name"]):
            if search_user_name == user:
                print(f"-----------------------\nName: {user}\nPhone: {self.library_dictionary['User']['User phone'][user_index]}\nUser standing: {self.library_dictionary['User']['User Standing'][user_index]}\n-----------------------")
                return
        print("User not found.")
    
    def display_user(self):
        print("Users:")
        for user in self.library_dictionary["User"]["User Name"]:
            print(f"{user}")
 
    def user_menu(self):  
        while True:  
            user_menu_selection = input("-----------------------------------\n 1. Add a new user\n 2. View user details\n 3. Display all users\n 4. Quit\n------------------------------------\n")
            if user_menu_selection == "1":
                self.add_user()
            elif user_menu_selection == "2":
                self.view_user()
            elif user_menu_selection == "3":
                self.display_user()
            elif user_menu_selection == "4":
                break
            else:
                print("Invalid selection. Please try again.")

# Class for Author
class Author:
    def __init__(self, library_dictionary):
        self.library_dictionary = library_dictionary
    
    def add_author(self):
        while True:  
            try:
                new_author = input("Add author: ")
                self.library_dictionary["Author"].append(new_author)
                print("Author added.")
                break
            except TypeError:
                print("Please type an author.")
    
    def view_author(self):
        search_author = input("Type author to view books: ")
        for author_index, author in enumerate(self.library_dictionary["Author"]):
            if author == search_author:
                author_books = [book for book_index, book in enumerate(self.library_dictionary["Book"]) if self.library_dictionary["Author"][book_index] == author]
                print(f"{author}: {author_books}")
                return
        print("Author not found.")
    
    def display_author(self):
        print("Authors:")
        for author in self.library_dictionary["Author"]:
            print(f"{author}")

    def author_menu(self):
        while True:  
            author_menu_selection = input("-----------------------------------\n 1. Add a new author\n 2. View author books\n 3. Display all authors\n 4. Quit\n------------------------------------\n")
            if author_menu_selection == "1":
                self.add_author()
            elif author_menu_selection == "2":
                self.view_author()
            elif author_menu_selection == "3":
                self.display_author()
            elif author_menu_selection == "4":
                break
            else:
                print("Invalid selection. Please try again.")

# Class for Genre
class Genre: 
    def __init__(self, library_genre):
        self.library_genre = library_genre
    
    def add_genre(self):
        while True:  
            try:
                new_genre = input("Add genre: ")
                description = input("Add genre description: ")
                self.library_genre[new_genre] = description
                print("Genre added.")
                break
            except TypeError:
                print("Please type a genre and description.")
        
    def display_genre(self):
        print("Genres:")
        for genre in self.library_genre:
            print(f"{genre}: {self.library_genre[genre]}")
 
    def view_genre(self):
        genre = input("Type genre as listed: ")
        if genre in self.library_genre:
            print(f"{genre}: {self.library_genre[genre]}")
        else:
            print("Genre not found.")
    
    def genre_menu(self):  
        while True:  
            genre_menu_selection = input("-----------------------------------\n 1. Add a new genre\n 2. View genre details\n 3. Display all genres\n 4. Quit\n------------------------------------\n")
            if genre_menu_selection == "1":
                self.add_genre()
            elif genre_menu_selection == "2":
                self.view_genre()
            elif genre_menu_selection == "3":
                self.display_genre()
            elif genre_menu_selection == "4":
                break
            else:
                print("Invalid selection. Please try again.")

# Class for Main Menu
class Main:
    def main_menu(self):
        while True:  
            main_menu_selection = input("-----------------------------------\n\tWelcome to the Contact Management System!\n Main Menu:\n 1. Book Menu\n 2. User Menu\n 3. Author Menu\n 4. Genre Menu\n 5. Quit\n------------------------------------\n")
            if main_menu_selection == "1":
                book_operations = Book(library_dictionary)
                book_operations.book_menu()
            elif main_menu_selection == "2":
                user_operations = User(library_dictionary)
                user_operations.user_menu()
            elif main_menu_selection == "3":
                author_operations = Author(library_dictionary)
                author_operations.author_menu()
            elif main_menu_selection == "4":
                genre_operations = Genre(library_genre)
                genre_operations.genre_menu()
            elif main_menu_selection == "5":
                sys.exit()
            else:
                print("Invalid selection. Please try again.")

# Call the main menu function
main_menu = Main()
main_menu.main_menu()



