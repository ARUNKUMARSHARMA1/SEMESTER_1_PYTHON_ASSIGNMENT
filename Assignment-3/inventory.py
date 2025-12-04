import json
import os
from book import Book

class Inventory:
    def __init__(self, filename="data.json"):
        self.filename = filename
        self.books = []
        self.load_data()

    def load_data(self):
        if not os.path.exists(self.filename):
            return
        with open(self.filename, "r") as f:
            data = json.load(f)
            self.books = [Book.from_dict(item) for item in data]

    def save_data(self):
        with open(self.filename, "w") as f:
            json.dump([b.to_dict() for b in self.books], f, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_data()

    def search(self, keyword):
        result = []
        for b in self.books:
            if (keyword.lower() in b.title.lower() or 
                keyword.lower() in b.author.lower() or
                keyword.lower() in b.genre.lower()):
                result.append(b)
        return result

    def issue_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn and b.copies > 0:
                b.copies -= 1
                self.save_data()
                return True
        return False

    def return_book(self, isbn):
        for b in self.books:
            if b.isbn == isbn:
                b.copies += 1
                self.save_data()
                return True
        return False

    def view_all(self):
        return self.books
