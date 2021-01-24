from behave import *

use_step_matcher("re")


@given("user inputs (?P<number>.+) and (?P<guess>.+)")
def step_impl(context, number, guess):
    context.number = int(number)
    context.user_guess = guess

@when("we run the converter")
def step_impl(context):
    try:
        context.res = context.roman.check_guess(context.number, context.user_guess)
    except TypeError as e:
        context.e = e 

@then("the result should be (?P<value>.+)")
def step_impl(context, value):
    assert str(context.res) == value
