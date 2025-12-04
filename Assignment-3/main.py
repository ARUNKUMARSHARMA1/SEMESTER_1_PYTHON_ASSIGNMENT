from inventory import Inventory
from book import Book

inv = Inventory()

def menu():
    print("\n===== Library Inventory Manager =====")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. View All Books")
    print("6. Exit")

if __name__ == "__main__":
    while True:
        menu()
        ch = input("Enter choice: ")

        if ch == "1":
            title = input("Title: ")
            author = input("Author: ")
            isbn = input("ISBN: ")
            genre = input("Genre: ")
            copies = int(input("Copies: "))
            book = Book(title, author, isbn, genre, copies)
            inv.add_book(book)
            print("Book added successfully!")

        elif ch == "2":
            key = input("Search keyword: ")
            result = inv.search(key)
            if result:
                for b in result:
                    print(f"{b.title} | {b.author} | {b.isbn} | {b.genre} | Copies: {b.copies}")
            else:
                print("No book found.")

        elif ch == "3":
            isbn = input("Enter ISBN to issue: ")
            if inv.issue_book(isbn):
                print("Book issued!")
            else:
                print("Book not available.")

        elif ch == "4":
            isbn = input("Enter ISBN to return: ")
            if inv.return_book(isbn):
                print("Book returned successfully!")
            else:
                print("Invalid ISBN.")

        elif ch == "5":
            books = inv.view_all()
            for b in books:
                print(f"{b.title} | {b.author} | {b.isbn} | {b.genre} | Copies: {b.copies}")

        elif ch == "6":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

