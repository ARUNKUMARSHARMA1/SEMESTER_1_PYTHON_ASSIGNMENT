class Book:
    def __init__(self, title, author, isbn, genre, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.copies = copies

    def to_dict(self):
        return {
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "genre": self.genre,
            "copies": self.copies
        }

    @staticmethod
    def from_dict(data):
        return Book(
            data["title"],
            data["author"],
            data["isbn"],
            data["genre"],
            data["copies"]
        )
