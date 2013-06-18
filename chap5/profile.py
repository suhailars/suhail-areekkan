import time

def fun(x):
      x=x*x
      print x

def profile(f):
    cache={}
    def g(x):
     tim=0
     if x not in cache:                         
      start = time.time()
      cache[x]=f(x)    
      tim=time.time()-start
     return tim 
    return g
f= profile(fun)
print f(4)
    
