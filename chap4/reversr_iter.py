class reverse_iter:
      def __init__(self,n):
           self.n = n
           self.i = len(n)-1
      def __iter__(self):
           return self
      def next(self):
            if self.i>=0:
               i=self.n[self.i]
               self.i -= 1
               return i
            else:
              raise StopIteration()
x = reverse_iter(['d','c','b','a'])
print x.next()
print x.next()
print x.next()
print x.next()
print x.next()
 
               
                 
