from behave import *
from src.zad4.Book import Book
from src.zad4.BookStorage import BookStorage

use_step_matcher("re")

@given("Database")
def step_impl(context):
    context.Book = Book(BookStorage())

@given("Baze danych")
def step_impl(context):
    context.Book = Book(BookStorage())

@given("a book with a correct IBNS number")
def step_impl(context):
    context.sample_book = {"title": "autobiografia andrzeja", "id": 1, "author": "Andrzej jakistam", "isbn": "978-0-1825-6947-2"}

@given("książke z poprawnym numerem isbn")
def step_impl(context):
    context.sample_book = {"title": "autobiografia andrzeja", "id": 1, "author": "Andrzej jakistam", "isbn": "978-0-1825-6947-2"}


@when("we add a book")
def step_impl(context):
    context.Book.add_book({"title": "autobiografia andrzeja", "id": 1, "author": "Andrzej jakistam", "isbn": "978-0-1825-6947-2"})

@when("dodamy książke")
def step_impl(context):
    context.Book.add_book({"title": "autobiografia andrzeja", "id": 1, "author": "Andrzej jakistam", "isbn": "978-0-1825-6947-2"})

@then("the book can be added")
def step_impl(context):
    assert context.Book.add_book(context.sample_book) == True

@then("książka sie dodaje")
def step_impl(context):
    assert context.Book.add_book(context.sample_book) == True

@then("the book can be deleted")
def step_impl(context):
    assert context.Book.delete_book(1) == True

@then("książka sie usuwa")
def step_impl(context):
    assert context.Book.delete_book(1) == True

@then("the books author can be retrieved")
def step_impl(context):
    print(context.Book.get_books_author(1))
    assert context.Book.get_books_author(1) == "Andrzej jakistam"


@then("autor książki może być odczytany")
def step_impl(context):
    print(context.Book.get_books_author(1))
    assert context.Book.get_books_author(1) == "Andrzej jakistam"
