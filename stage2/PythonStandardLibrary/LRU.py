#its a funciton result caching mechanism

#It remembers the results of previous 
#function calls so that the function doesn't need to calculate the same result again.
from functools import lru_cache
@lru_cache(maxsize=1024)
def fib(n):
    if(n<=1):
        return n
    return fib(n-1)+fib(n-2)
print(fib(1001))
#print(fib.cache_info())