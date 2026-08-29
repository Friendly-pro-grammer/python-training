import time
from logger import logger
def logging_decorator(func):
    def wrapper():
        print("logging action")
        func()
        print("after call action")
    return wrapper
@logging_decorator
def greet():
    print("hello")
# greet1 = logging_decorator(greet)
greet()

def timer(func):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        end = time.time()
        print(f"Execution time {end-start:.8f}s ",end-start)
        return result
    return wrapper
@timer
def counter_1000():
    sum=0
    for i in range(1,100000000):
        sum+=i
    print(sum)
counter_1000()
@logger
def add(a,b):
    return a+b
add(a=10,b=20)