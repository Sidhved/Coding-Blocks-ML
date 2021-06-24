import Calculator

print(Calculator.add(1, 2))
print(Calculator.sub(1, 2))
print(Calculator.mul(1, 2))
print(Calculator.div (1, 2))

# different ways for importing modules aka filter import

from Calculator import add

print(add(1, 2))

# importing all the methods from a module
from Calculator import *   # not recommended since not explicit enough

print(Calculator)

# Aliases

def Calculator(a, b):
    print(a, b)

import Calculator as cal        # this can also be applied to filtered import
print(cal.add(1, 4))