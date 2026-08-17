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
while(j<10):
    if(j==6):
        pass
    elif(j==7):
        continue
    print(j)
    j+=1


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
