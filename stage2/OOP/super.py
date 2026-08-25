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
    def __init__(self, price, brand, model,ram,storage):
        super().__init__(price, brand, model)
        self.ram=ram
        self.storage = storage
    def buy(self):
        print("buying a smartphone")
        super().buy()#access parents methods and constructor not attributes
s = SmartPhone(15000,"Xioami","Redmi Note 11",12,256)