#basic function
def fun_name(arguments):
    #function body
    print(arguments)
def greet(name):
    print("hello"+" "+name)
def tempfn():
    pass
greet("amit")#function calling
#returning function
def ret_square(n):
    return n**2
print(ret_square(5))
#parameter-value defined in function
#arguments-actual value passed in function
def add(a,b):
    return a+b
# a function by default returns none
res = tempfn()
print(res)
#return multiple values
def get_user():
    return "amit",22
name,age = get_user()
print(name,age)
#default parameter
def user_info(name="amit"):
    print(name)
user_info()
#keyword arguments 
def introduce(name,age):
    print(name,age)
introduce(name="amit",age=22)
#positional arguments
introduce("amit",age=22)
#positional should be before the keyword arguments

#args in python
#accept any number of positional arguments
def arg1(*args):
    print(args)
arg1(10,20,30,"hlo")
#its basically a tuple of provided arguments
def total_sum(*args):
    total=0
    for num in args:
        total+=num
    print(total)
total_sum(10,100,343,235,4,456,45,6)
#with normal parameters
def exmpl(first,*args):
    print("first:",first)
    print("rem:",args)
exmpl(1,2,3,4,5,66)

#kwargs in python
#similar to args but just with keywords
def show_info(**kwargs):
    print(kwargs)
show_info(name="amit",age=22,email="example@gmail.com")
#returns a object/dict

#argument unpacking
def add1(a,b,c):
    print(a+b+c)
numbers = [10,20,30]
add1(*numbers)

#** unpacking
def intro(name,age,city):
    print(name,age+1,city)
person={
    "name":"amit",
    "age":22,
    "city":"gandhidham"
}

intro(**person)