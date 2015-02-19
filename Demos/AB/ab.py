#!/usr/bin/env python3

# class A
# class B has some properties
# one of which is an instance of A
# class B { 
#     mya=A()
#  }
#  an instance of B, therefore will have an instance of A as a property

# I need to access the instance of B from the instance of A
# so like myB=B()
# myB.myA.<SOMEMETHOD> yields myB

class A:
    def __init__(self, value):
        self.value = value

class B:
    def __init__(self, value):
        self.value = self, value

mya = A("I am an instance of A")
myb = B(mya)

print (">>> print(A)")
print (A)

print (">>> print(mya.value)")
print (mya.value)

print (">>> print(B)")
print (B)

print ("### Note next we get back a tuple, the 0th entry is mya, the 1st is myb")
print (">>> print(myb.value)")
print (myb.value)

print ("### So we can get both bits explicitly, to capture both the A and B instances")
print (">>> foo,bar = myb.value")
(foo,bar) = myb.value

print (">>> print (foo.value)")
print (foo.value)

print (">>> print (bar.value)")
print (bar.value)

print ("### Or, looking a little ugly (I'd comment this) we can do it all in one line.")
print (">>> print (myb.value[1].value)")
print (myb.value[1].value)

