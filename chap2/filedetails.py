import os
import time
import re

def filedetail(d):
    lis=[] 
    f=os.listdir(d)
    for i in f:
      path=os.path.abspath(os.path.join(d, i))
      lis.append(path)
    for i in lis:
      t=open(i,'r')  
      text=t.read()  
      print os.path.basename(i),'\n',time.ctime(os.path.getmtime(i)),'\n',len(text)
      t.close()
filedetail('suh')
       
