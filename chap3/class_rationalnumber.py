class RationalNumber:
    
    def __init__(self, numerator, denominator=1):
        self.n = numerator
        self.d = denominator

    def __add__(self, other):
        if not isinstance(other, RationalNumber):
            other = RationalNumber(other)

        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return RationalNumber(n, d)
   
    def __sub__(self,other): 
        if not isinstance(other,RationalNumber):
          other = RationalNumber(other)
        n = self.n * other.d + self.d * other.n
        d = self.d * other.d
        return RationalNumber(n, d)
    

    def __str__(self):
        return "%s/%s" % (self.n,self.d)
    __rep__ = __str__
a = RationalNumber(3,2)
b = RationalNumber(3)
c=2
print"addition with other", b+c
print "addtion", a+b
print "subtraction",a-b

