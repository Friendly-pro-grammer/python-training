#if statements
x=int(input("enter your age"))
if x<=0:
    print("invalid age")
elif x>100:
    print("enter your real age")

#if-else statements
amount=1000
if amount<100:
    print("cheap")
elif amount==0:
    print("free")
else:
    print("expensive")

#loops
#for loop
words = ["apple","boy","car","dog"]
for word in words:
    print(word)
#range function
for i in range(10):
    print(i)
#prints 0 to 9
for i in range(1,11):
    print(i)
#prints 1 to 10
str1 = "hello world"
for ch in str1:
    print(ch)
#list using the range function
#range(start,stop,step)
l1 = list(range(5,101,5))
for i in range(len(l1)):
    print(l1[i])
#break and continue
for i in range(1,101):
    if(i==50):
        break
    else:
        print(i)
#continue
for i in range(1,11):
    if(i==5):
        continue
    else:
        print(i)
#while loop
i=1
while(i<5):
    print(i)
    i+=1
j=5
# while(j<10):
#     if(j==6):
#         pass
#     elif(j==7):
#         continue
#     print(j)
#     j+=1


#for else loop concept
for i in range(5):
    print(i)
else:
    print("loop finished")
    
#prime numbers loop
prime = 50
for i in range(2,prime):
    if(prime%i==0):
        print("not prime")
        break
else:
    print("prime")
#for loops else is executed only when the loop is terminated normally not by the break statement if it
#gets terminated normally the else part gets executed and we can see that the number is prime ..

#inbuilt and lamba functions
#inbuilt-print,len,type,sum,max,min
list2=[9,66,4,33,22,65,3,7,8,87]
print(len(list2))
print(min(list2))
print(max(list2))
print(sum(list2))
print(abs(-10))
print(round(3.1415129))
print(pow(2,3))
print(sorted(list2))

#map
def double(x):
    return x*2
result1 = map(double,list2)
print(list(result1))
#lambda functions
square_fun= lambda x:x*x
print(square_fun(5))
#lambda arguments:expression
list3 = [1,4,9,16,25,36,49,64,81,100]
result2 = map(lambda x:x**0.5,list3)
print(list(result2))
#filter function used filters the elements based on the specific conditions
result3 = filter(lambda x:x%2==0,list3)
print(list(result3))

