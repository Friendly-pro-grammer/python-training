class User:
    def __init__(self):
        pass
    def login(self):
        print("Login")
    def Register(self):
        print("Register")
class Student(User):
    def __init__(self):
        pass
    def enroll(self):
        print("Enroll")
    def review(self):
        print("review")
    
stu1 = Student()
stu1.enroll()
stu1.login()


#-------------Inheriting a constructor-------------
class Phone:
    def __init__(self,price,brand,model):
        print("inside the phone constructor")
        self.price = price
        self.brand = brand
        self.model = model
    def buy(self):
        print("buying a  phone")
    def sell(self):
        print("selling a phone")
class SmartPhone(Phone):
    pass
s = SmartPhone(15000,"Xioami","Redmi Note 11")
#also child class object cannnot access hidden memebers of the parent class