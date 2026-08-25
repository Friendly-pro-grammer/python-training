from itertools import *

numbers= [1,2,3,4]

result = combinations(numbers,3)
#generate all possible selection of r elements
for i in result:
    print(i)

print(list(combinations_with_replacement([1,2,3],3)))

print(list(permutations([1,2,3])))


#product -to produce cartesian products

colors = ["red","green","blue"]
sizes = ["xs","s","m","l","xl","xxl"]
print(list(product(colors,sizes)))

print(list(product([0,1],repeat=3)))

print(list(chain([1,2,3],[4,5,6],[7,8,9])))

print(list(repeat('a',5)))