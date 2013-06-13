import sys
def group(lis,n):
    t=0
    s=[]
    k=len(lis)
    
    
   
    for i in lis[:n]:
       if lis.index(i) == k-1:
          s.append(i)
          print s
          sys.exit(0) 
       else:
          s.append(i)
       
    print s
            
    lis=lis[n:]
    group(lis,n) 




#print a
group(sys.argv[1],3)           
