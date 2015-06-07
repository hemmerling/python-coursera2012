#!/usr/bin/env python
x = 5
def a(y):
    global x
    x = x + y
    return y
def c(y):
    return x + y
def b(x,y):
    x = x + y
    return x
def d(y):
    y = x + y
    return y
print a(5), b(6,5),c(5),d(5)
