#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# The requests library is a really commonly used third party library for making HTTP / HTTPS and other
# web type requests.
import requests

# copy is part of the python standard library, and allows us to make duplicates of objects
# (either variables, or instances of classes). This is useful as a = b doesn't actually make a copy of b
# it just results in a and b pointing to the same object.
import copy

# Here we define the money class, which is the point of this example.
class Money:
    # This is the magic method that gets called when we make new instances of the Money class.
    # We can set the name of the currency (which should be the standard three letter code)
    # We can set the symbol used, and the numeric value as well.
    # By having values in the function definition we can have default values.
    # Therefore, if you just do a = Money(), in this example, a will be one US dollar.
    def __init__(self, name="USD", symbol="$", numericvalue=1):
        self.name = name
        self.symbol = symbol
        self.numericvalue = numericvalue

    def convert(self, name="USD", symbol="$"):
    # This method returns a new Money object based on converting the object it is called on into
    # the currency type specified.
        response = requests.get("http://rate-exchange.appspot.com/currency?from=" + self.name + "&to=" + name)
        rate = response.json()["rate"]
        return Money(name=name, symbol=symbol, numericvalue=self.numericvalue * rate)

    def __gt__(self, other):
        # This allows us to compare two Money objects
        # In the comparisson a > b for example
        # self is a, and other is b
        # We can then do whatever we like, returning True if a > b
        # and returning false otherwise.
        if self.convert("USD").numericvalue > other.convert("USD").numericvalue:
            return True
        else:
            return False

    def __eq__(self, other):
        # Very similar to the __gt__ magic method, except here we look for
        # equality rather than greater than. As you can see, it is much simpler.
        if (self.convert("USD") == other.convert("USD")):
            return True
        else:
            return False

    def __add__(self, other):
        # This allows us to perform addition on two Money objects
        # If they are in different currencies, we return the object in the first
        # currency. a + b will return the result in currency a.

        # Copy otherwise returncurrency is just a ref to self, and when we
        # modify returncurrency, we also modify self.
        returncurrency = copy.copy(self)
        # The case when the currencies are the same is easy.
        if (self.name == other.name):
            returncurrency.numericvalue = self.numericvalue + other.numericvalue
            return returncurrency
        # When they are different, we convert b to a
        # and then call this again. That way the example above gets run.
        else:
            otherconverted = other.convert(self.name)
            returncurrency = self + otherconverted
            return returncurrency

    def __repr__(self):
        # This is what is returned when we try and print or otherwise
        # represent the money object. If we don't do that, we just get told
        # we have a money object with no details of what is inside it.
        return self.symbol + str(round(self.numericvalue,2))

###################################################################

# This is code that gets run if we run the currency.py script
# This construct means if we import currency into another
# script, this code DOES NOT get run.
# This allows us to do things like build this demo code.
if __name__ == '__main__':
    # We define a set of money objects.
    onepound = Money(name="GBP", symbol="£", numericvalue=1)
    onedollar = Money(name="USD", symbol="$", numericvalue=1)
    onemillionyen = Money(name="JPY", symbol="¥", numericvalue=1000000)

    # Here are some examples of us comparing Money objects.
    if (onepound > onedollar):
        print (onepound, "is worth more than ", onedollar)
    if (onedollar > onepound):
        print (onedollar, "is worth more than ", onepound)
    if (onemillionyen > onepound):
        print (onemillionyen, "is worth more than ", onepound)
    # Note even though we haven't defined __lt__, we can still do
    # a less than check. Python knows if a is not greater than b, and
    # a is not equal to b, a must be less than b. Therefore, for all the
    # compare operations like <=, <, >, >= and == to work, you only
    # need to define the equality check and one of the others.
    if (onemillionyen < onepound):
        print (onepound, "is worth more than ", onemillionyen)

    # Here we have examples of adding up money.
    print ("{0} + {1} = {2}".format(onepound, onepound, onepound + onepound))
    print ("{0} + {1} = {2}".format(onepound, onedollar, onepound + onedollar))
    print ("{0} + {1} = {2}".format(onedollar, onepound, onedollar + onepound))
    print ("{0} + {1} = {2}".format(onedollar, onemillionyen, onedollar + onemillionyen))

# For a fully featured currency class, I would recommend you look at one of :-
# https://code.google.com/p/python-money/
# or
# http://quantlib.org/index.shtml

# Improvements.
# A Currency (as in US Dollars) should be different from
# an amount of Money (as in 1 US Dollar).
# This would allow you to only pass the currency type into
# a function like convert instead of duplicating data all the time.