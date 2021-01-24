from src.zad3.isbn import Isbn

class Book(object):
    def __init__(self, book_storage = None):
        self.book_storage = book_storage
        self.isbn = Isbn()

    def add_book(self, book):
        if self.isbn.is_valid(book["isbn"]):
            return self.book_storage.add(book)
        return "invalid isbn number"

    def delete_book(self, book_id):
        book = self.book_storage.find(book_id)

        if book:
            self.book_storage.delete(book)
            return True

        return False

    def get_all_books(self):
        return self.book_storage.find()

    def get_book_by_id(self, book_id):
        if type(book_id) is not int or book_id < 0:
            return "Book_id is incorrect"

        res = self.book_storage.find(book_id)
        if res:
            return res
        else:
            return "Book not found"

    def get_books_title(self, book_id):
        book = self.get_book_by_id(book_id)

        if isinstance(book, list):
            return book["title"]
        
        return book

    def get_books_author(self, book_id):
        book = self.get_book_by_id(book_id)

        return book["author"]
