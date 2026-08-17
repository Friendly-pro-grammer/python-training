#hello world
print("hello world")
a=3456789
b=3456789
a=[]
b=[]
print(a is b)
print(id(a),id(b))


#obj has three attributes - id,type,value
name= "amit"
print(id(name))
print(type(name))
print(name)

#mutable and immutable
#immmutable - numbers,string,tuples(unchangeable)
list1 = [1,2,3,4,5]
list1[0]=3
print(id(list[0]),id(list[1]))

tup=([1,2],3,4,5)
tup[0].append(3)

#types in python
#none type
x=None
print(bool(x))
#int
n1=100
n2=-50
print(type(n1))
#bool
t1=True
t2=False
print((t1==1))
print(bool("False"))
#float
f1=3.1415129
#complex
z1=3+4j
print(z1.real,z1.imag)
#sequences =str,tuples,bytes,list
#strings
s1="hello"
s2="world"
s1=s1+s2
print(s1)
print(ord('a'))
print(chr(65))
print(s1.encode())

#tuples 
#immutable sequence
tup1=(1,2,3,4,5)
tup2=(1,)
#mutable sequences
#List
numbers=[10,"hello",3.14,True]
#can store multiple type objects
#sets
st1={1,23,45}
st2=set()



#operators
q=10
w=20
print(q+w)
print(q-w)
print(q*w)
print(q**2,w**2)
print(q/w)
print(q//w)
print(w%q)
#comparision operators
print(q==w)
print(q!=w)
print(q<w)
print(q>w)
print(q<=w)
print(q>=w)

#logical operators
age=22
print(age>18 or age<25)
print(age>18 and age<25)
print(not(age>18))


#assignment operators
i=1
i+=1
i*=2
i**=2
print(i)
#identity operatorss
l1=[1,3]
l2=l1
print(l1 is not l2)

#membership operator
name1 = "python"
print("oh" in name1)
print("" in name1)


#type conversion
w1 = "100"
y1 = int(w1)
