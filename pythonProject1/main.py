from utils import database

USER_CHOICE = """
Enter:
-"a" to add a new book 
-"l" to list all books
-"r" to mark books as read
-"d" to delete a book 
-"q" to quit 

Yor choice: """

def menu():
    database.create_book_table()
    user_input=input(USER_CHOICE)
    while user_input != "q":
        if user_input == "a":
            prompt_add_book()
        elif user_input =="l":
            list_book()
        elif user_input =="r":
            prompt_read_book()
        elif user_input =="d":
            prompt_delete_book()
        elif user_input =="q":
            pass
        else:
            print("Unknown command.Please try again.")

        user_input=input(USER_CHOICE)


def prompt_add_book():
    name= input("Enter the book name:")
    author=input("Enter the author:")

    database.add_book(name,author)

def list_book():
    books= database.get_all_books()
    for book in books:
        read= 'YES' if book['read'] =="1" else "NO"
        print(f"{book['name']} by {book['author']},read {read} ")

def prompt_read_book():
    name=input("Enter the name of the book:")

    database.mark_book_as_read(name)

def prompt_delete_book():
    name=input("Enter the name of the book:")

    database.delete_book(name)


menu()
