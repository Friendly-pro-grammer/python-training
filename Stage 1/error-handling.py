#try-catch block

try:
    x=10/0
except ZeroDivisionError:
    print("cannot divide by zero")
    
def num_print():
    try:
        number = int(input("enter number"))
        print(number)
    except ValueError:
        print("invalid value")
    else:
        print("success",number)

#finally block
try:
    x=10/2
except ZeroDivisionError:
    print("cannot divide by zero")
finally:
    print("this always execute")
#raising exceptions manually
class InvalidAgeError(Exception):
    pass
age = 21
def can_vote(age):
    if(age<18):
        raise InvalidAgeError("Minors cant vote")
    else:
        print("you can vote")    
print(can_vote(75))

#raising multiple errors
try:
    x=int(input("enter a number"))
except (ValueError,TypeError) as e:
    print(e)
else:
    print(x**2)
