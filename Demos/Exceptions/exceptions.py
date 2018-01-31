#!/usr/bin/env python3

import traceback

a = "string"    # a string
b = 3           # an integer

# We can't add these together. We expect an error and will get one.

try:
    c = a + b
except Exception as e:
    print("Something went wrong adding those things together !")
    print("Python said it was ...")
    print(traceback.print_exc())

print("")
print("We can continue to do something else, but c is still undefined remember !")
print("So this will fail")

print(c)

print("And this will never run")