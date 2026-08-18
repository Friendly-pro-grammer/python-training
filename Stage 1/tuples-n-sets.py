#tuples-ordered but immutable container
numbers=(10,20,30,40,50)
#same accessing methods as list
empty=()
#it can aslo store multiple types of data
t1 = (10,"helllo",3.14,True)
x=(10)# this is not a tuple
x=(10,)#this is a tuple
#also paranthesis are optional
t2 = 10,20,30
#this is also a tuple
print(t2)
#is called tuple packing
#tuple unpacking
a,b,c=t2
t3 = 1,2,3,4,5,6,7,8,9,0
d,*rest = t3
print(d)
print(rest)
#same slicing and indexing as list
print(t3[1:3])
t3[::-1]#reverses the tuple
# a tuple is immutable but it contains mutable object 
t4 = (1,2,[3,4],5)
t4[2].append(6)
print(t4)
#tuple methods-count and index
print(t3.count(1))
print(t3.index(5))
#some other methods
print(len(t3))
print(5 in t3)

#----------sets----------------

#set is a unordered collection of unique elements
s1 = {1,2,3,4,5}
s2 = set()
#empty set
l1=[1,2,3,4,5,6,5,4,3,1]
print(set(l1))
#converting to the set does not preserve originak ordering 
#set elements should be hashable
#add elements to set
s2.add(4)
#add multiple elements in set
s2.update([4,5,6])
s2.update((7,8))
s2.update({8,9})
#remove elements from the set
print(s2)
s2.remove(8)
#but remove throws an error of the element doesnt exist
# to remove the element without worrying about an error
s2.discard(50)
#remove all elements
s1.clear()


#set operations
a={1,2,3,4}
b={3,4,5,6}

#union
print(a|b)
print(a.union(b))
#intersection
print(a&b)
print(a.intersection(b))
#difference
print(a-b)
print(a.difference(b))
#symmetric difference
print(a^b)
c = {1,2,3,4,5,6,7}
d={4,7}
print(c.issubset(d))
#disjoint sets have nithing in commons
print(a.isdisjoint(d))
#set comprehension also works it removes duplicates
values = {x%2 for x in range(1,101)}
print(values)
