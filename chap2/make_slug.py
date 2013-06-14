import re
import sys
def make_slug(str1):
     l=[]
     l1=[]
     l=str1.split()
     t=''
     for i in l:
       match=re.search('\w+',i)
       l1.append(match.group())
     for i in l1:
       if i != l1[-1]:
        t=t+i+'-'
       else:
         t=t+i 
     print t
make_slug(sys.argv[1])       
