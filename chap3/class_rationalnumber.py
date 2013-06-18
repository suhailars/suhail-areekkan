class RationalNumber:
    """
    Rational Numbers with support for arthmetic operations.

        >>> a = RationalNumber(1, 2)
        >>> b = RationalNumber(1, 3)
        >>> a + b
        5/6
        >>> a - b
        1/6
        >>> a * b
        1/6
        >>> a/b
        3/2
    """
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
        n = self.n * other.d - self.d * other.n
        d = self.d * other.d
        return RationalNumber(n, d)
    

    def __str__(self):
        return "%s/%s" % (self.n,self.d)
    __rep__ = __str__
a = RationalNumber(3,2)
#a=6
b = RationalNumber(3)
c=2
print b+c
print a+b
print a-b
#print a.__str__()
