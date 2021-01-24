from behave import *
from src.zad1.roman import Roman
from src.zad3.isbn import Isbn

def before_scenario(context, scenario):
    context.roman = Roman()
    context.isbn = Isbn()

def after_scenario(context, scenario):
    context.roman = None
    context.isbn = None