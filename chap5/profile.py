import time
def fib(n):
    if n is 0 or n is 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def profile(f):
    cache={}
    def g(x):
     tim=0
     if x not in cache:                         
      start = time.time()
      cache[x]=f(x)    
      tim=time.time()-start
     return str(tim)+' sec' 
    return g
f= profile(fib)
print f(20)
    
