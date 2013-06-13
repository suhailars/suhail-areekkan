def triplet(n):
    l=[]  
    for a in range(1,n):
      k=n
      for b in range(1,k):
        c=n-a-b
        t=()
        if c <= a+b and a+b<n:
           t=(a,b,a+b)
           l.append(t) 
      k-=2
    print l 
            
triplet(5)
        
               
