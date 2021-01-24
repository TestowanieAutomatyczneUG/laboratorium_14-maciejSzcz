from behave import *

use_step_matcher("re")


@given("user inputs isbn (?P<number>.+)")
def step_impl(context, number):
    context.number = number


@when("we run the validator")
def step_impl(context):

    context.res = context.isbn.is_valid(context.number)


@then("the result of validation should be (?P<value>.+)")
def step_impl(context, value):
    assert str(context.res) == value
