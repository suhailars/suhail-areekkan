import sys
def peep(itr):
 l=[]
 try:
   for i in range(100):
      l.append(itr.next())
 except:print ''
 finally:
   l.insert(0,l[0])
   t=iter(l)
   x=t.next()
   return x,t
itr=iter(range(5))
x,it=peep(itr)    
print x,list(it)
