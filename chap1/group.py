import sys
import ast

def group(lis,n,t=[]):
    s=[]
    k=len(lis)
    for i in lis[:n]:
       if lis.index(i) == k-1:
          s.append(i)
          t.append(s)
          print t
          sys.exit(0) 
       else:
          s.append(i)
       
    t.append(s) 
    lis=lis[n:]
    group(lis,n,t) 

def readlist(x):
     x=ast.literal_eval(x)
     return x 
     
       
x=readlist(sys.argv[1])
#print x

group(x,int(sys.argv[2]))           
