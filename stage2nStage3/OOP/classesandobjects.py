import sys
class Atm:
    __counter = 1
    def __init__(self):
        self.__pin=""
        self.__balance = 0
        self.serial_no = Atm.counter
        Atm.__counter = Atm.__counter+1
        #self.menu()
    @staticmethod
    def get_counter():
        return Atm.__counter
    @staticmethod
    def set_counter(val):
        if(isinstance(val,int)):
            Atm.__counter=val
        else:
            raise ValueError("please provide a valid counter value")
    def menu(self):
        while True:
            print("""
                Select a option
                1.Create PIN
                2.Deposit
                3.Withdraw
                4.Check Balance
                5.Exit
                """)
            option = int(input("Select a option from above"))
            match option:
                case 1:
                    self.set_pin()
                case 2:
                    self.deposit()
                case 3:
                    self.withdraw()
                case 4:
                    self.check_balance()
                case 5:
                    self.exit_menu()
                case _:
                    self.throw_error()
    def set_pin(self):
        pin_set = int(input("Plese enter the pin"))
        self.__pin = pin_set
        print("PIN set successfully")
    def check_pin(self):
        pin_provided = int(input("please enter yout PIN"))
        return pin_provided == self.__pin
    def deposit(self):
        if(self.check_pin()):
            amount = int(input("please enter the amount to deposit"))
            self.__balance = self.__balance+amount
            print("operation successfull")
        else:
            print("please provide the correct pin") 
    def withdraw(self):
        if(self.check_pin()):
            amount = int(input("please enter the amount to deposit"))
            if(amount<self.balance):
                self.__balance = self.__balance-amount
                print("operationn successfull")
            else:
                print("insufficient funds")
        else:
            print("please provide the correct pin")
    def check_balance(self):
        if(self.check_pin()):
            print("availaible balance: "+ str(self.__balance))
        else:
            print("please provide the correct pin")
    def exit_menu(self):
        print("Exiting Application Have a good day")
        sys.exit()
