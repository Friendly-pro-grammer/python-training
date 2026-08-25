from functools import *

#partial function creates new function with some arguments already filled in
def power(base,exponent):
    return base**exponent

#suppose you want to calculate squares or cubes

square = partial(power,exponent=2)
cube = partial(power,exponent=3)
print(square(5))
print(square(10))
print(cube(3))