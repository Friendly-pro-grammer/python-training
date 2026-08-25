from functools import *
#applies a function to a iterable to reduce its value to final
number=list(range(1,101))
result = reduce(lambda a,b:a+b,number)
print(result)
print(sum(number))

