import calculator

result = calculator.add(10,12342)
print(result)

result2=calculator.subtract(10,42)
print(result2)

#or use this
from calculator import multiply
x = multiply(10,5)

#or import everything at once
from calculator import *

#or use aliases
import calculator as calc
