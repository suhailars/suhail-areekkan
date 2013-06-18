def square(x): return x * x
def vectorize(f):
    cache={}
    l=[]  
    def g(x):
        k=0  
        for i in x:
            if isinstance(i,list):
             k=x.index(i)
             cache[k]=f(i)
             l.append(cache[k])   
            else :
             cache[k]=f(i)
             l.append(cache[k])

        return  l
    return g
f = vectorize(square)
print f([1,2,3])
g = vectorize(len)
#print g(["hello", "world"])
print g([[1, 2], [2, 3, 4]])
