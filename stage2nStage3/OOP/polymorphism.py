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
    #same name method overridden
    def buy(self):
        print("Buying a smartphone")
s = SmartPhone(15000,"Xioami","Redmi Note 11")
s.buy()
#method overloading and operator overloading
#1
#different input different behaviour
class Geometry:
    def area(self,radius):
        return 3.14*radius*radius
    def area(self,a,b):
        return l*b
obj = Geometry()
print(obj.area(5))
#doesnt works here
#workaround for the method overloading
class Geometry1:    
    def area(self,l,b=0):
        if(b==0):
            print("circle",3.14*l*l)
        else:
            print("rectangle",l*b)
#operator overloading
#use magic methods use __str__,__add__
print("hello"+"world")