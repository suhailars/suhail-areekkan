def cumsum(a):
    pr=[]
    s=[]
    k=0
    m=0
    p=0
    for i in a:
      l=[]
      k=a.index(i)
      
      l=a[:k+1]
      print l
      m=sum(l)
      p=product(l)
      #for r in l:
        # m = m + r  
      s.append(m)
      pr.append(p)   
    print s,pr
def product(a):
    p=1
    for i in a:
     p=p*i
    return p
a=[1,2,3,4]
cumsum(a)     

