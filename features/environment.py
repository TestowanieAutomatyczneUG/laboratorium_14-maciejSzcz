from behave import *
from src.zad1.roman import Roman

def before_scenario(context, scenario):
    context.roman = Roman()

def after_scenario(context, scenario):
    context.roman = None
