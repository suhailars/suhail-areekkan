class Bankaccount:
       def __init__(self):
             self.balance=0
             self.intrest=0.0
       def withdraw(self,amount):
           self.balance -= amount
           self.intrest += float (self.balance/100)  

           return self.balance,self.intrest
       def deposite(self,amount):
           self.balance += amount
           self.intrest +=float (self.balance/100)
           return self.balance,self.intrest
class minbalance(Bankaccount):
       def __init__(self,minbal):
          Bankaccount.__init__(self)
          self.minbal=minbal
       def withdraw(self,amount):
           if self.minbal > self.balance-amount:
                 print 'action denied!!!keep mininmum balance'
           else:
            return  Bankaccount.withdraw(self,amount)
          
a = Bankaccount()
b = Bankaccount()
d = minbalance(60)
print a.deposite(100)
print b.deposite(50) 
print a.withdraw(50)
print b.withdraw(0)
print d.deposite(100)
print d.withdraw(40)

     
          
