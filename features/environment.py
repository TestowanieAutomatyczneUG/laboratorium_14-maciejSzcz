from behave import *
from src.zad1.roman import Roman
from src.zad3.isbn import Isbn
from src.zad4.Book import Book
from src.zad4.BookStorage import BookStorage

def before_scenario(context, scenario):
    context.roman = Roman()
    context.isbn = Isbn()
    context.Book = Book(BookStorage)

def after_scenario(context, scenario):
    context.roman = None
    context.isbn = None