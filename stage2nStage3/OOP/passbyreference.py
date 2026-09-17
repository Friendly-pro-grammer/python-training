class Customer:
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender
def greet(cust):
    if(cust.gender=="male"):
        print("hello"+cust.name+"sir")
    else:
        print("hello "+cust.name+" mam")
    
cust = Customer("Amit","male")
greet(cust)