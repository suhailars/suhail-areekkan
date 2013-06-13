import sys
d=int(sys.argv[2])
def wrap(filename):
    f=open(filename,'r')
    t=f.readlines()
    for i in t:
       if len(i)>d:
        wrap1(i)
       else :
        print i
def wrap1(a):
   while(len(a)>d):
     print a[:d]
     a='\n'+a[d:]  
wrap(sys.argv[1])
