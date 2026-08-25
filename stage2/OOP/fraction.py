class Fraction:
    def __init__(self,n,d):
        self.numerator = n
        self.denominator =d
    def __str__(self):
        return "{}/{}".format(self.numerator,self.denominator)
    def __add__(self, other):
        temp_num = (self.numerator*other.denominator)+(other.numerator*self.denominator)
        temp_den= self.denominator*other.denominator
        return"{}/{}".format(temp_num,temp_den)
    def __sub__(self, other):
        temp_num = (self.numerator*other.denominator)-(other.numerator*self.denominator)
        temp_den= self.denominator*other.denominator
        return"{}/{}".format(temp_num,temp_den)
    def __mul__(self, other):
        temp_num = self.numerator*other.numerator
        temp_den= self.denominator*other.denominator
        return"{}/{}".format(temp_num,temp_den)
    def __truediv__(self, other):
        temp_num  = self.numerator*other.denominator
        temp_den = self.denominator*other.numerator
        return"{}/{}".format(temp_num,temp_den)