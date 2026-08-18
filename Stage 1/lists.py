import copy
#list is a ordered mutable collection of objects
numbers = [10,20,30,40,50]
#accessing in list
print(numbers[0])
print(numbers[1])
#Lists are ordered so they preserve the order of the elements they are stored in
#changing lists 
numbers[0]=90
print(numbers)
#list can store different types
l1 = [10,"hello",3.14,True]
#list inside a list
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
#accesing a 2d list
print(matrix[0][0])
print(len(matrix[0]))
print(matrix[2][2])
#empty list
numbers1=[]
numbers2=list()
#convert into list
chars = list("python")
print(chars)
#list uses zero based indexing
#list supports negative indexing also -1 represents last elements
print(chars[-1])
print(chars[-2])

#list slicing
#list[start:stop] stop element is not included
l1 = list(range(1,101))
print(l1[0:51])
#list[start:stop:step]
print(l1[1:100:2])
#reverse a list using slicing
print(numbers[::-1])


#add elements to the list
numbers.append(10)
#numbers.append([4,5])#ads[4,5] will be added as a single element 
numbers.extend([6,7])# adds 6,7 as separate elements using an iterator
#numbers.extend("ABC")
print(numbers)
#numbers.remove('B')
#numbers.remove('C')
#to add a element at a specific postion list.insert(index,value)
numbers.insert(2,20)

#remove an element ,remove deletes the first occurence of the element
numbers.remove(20)

#pop removes and returns an element 
x = numbers.pop()
#or use pop with an index
value = numbers.pop(5)

#using del to remove a element
del numbers[1]

#use index to get the index of specific element
print(numbers.index(6))

#count to get count of element
print(numbers.count(90))

#sort in place
numbers.sort()

#sort descending
numbers.sort(reverse=True)
#sort modifies the original list and returns None
#whereas sorted returns the sorted list doesnt changes the original list
res_sorted = sorted(numbers)

#sort using a key
students = [
    ("amit",111),
    ("rahul",112),
    ("john",113)
]
students.sort(key=lambda student:student[1])


#reverse a list
l1.reverse()
#it does in place 
#to do it using a new list just use
reversed1 = reversed(l1)

#membership operator ti check if an element exists in the list
print(20 in numbers)

#iterate over a list
list2 = [1,2,3,4,4,5,6,7,8]
for i in range(len(list2)):
    print(i,list2[i])
for nums in list2:
    print(nums)
    
#concat a list
l12 = [1,2]+[3,4]

#copying lists
a=[1,2,3]
b=a
print(a==b)
#shallow copy new list
c = a.copy()
#deepcopy
d = copy.deepcopy(a)


##------list-----comprehension---------
#[expression for item in iterable]
squares=[x*x for x in range(5)]
print(squares)
#comprehension with conditions
even_numbers = [x for x in range(101) if x%2==0]
print(even_numbers)
#list comprehension with if/else
result = ["even" if x%2==0 else "odd" for x in range(5)]