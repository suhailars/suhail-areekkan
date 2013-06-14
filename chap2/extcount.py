import os
import re
import sys
def excount(d):
    list1=[]
    list2=[]
    dict1={}
    f=os.listdir(d)
    for i in f:
      list1.append(i)
    for i in list1:
       match=re.search('.(\w+)',i)
       list2.append(match.group(1))
    for i in list2:
        if i not in dict1:
         dict1[i]=1
        else:
          dict1[i]+=1
    for i,j in dict1.items():
     print i,' ',j     
    
excount(sys.argv[1])
