import re
def strip(filename):
    f=open(filename,'r')
    for line in f:
         match = re.sub("<.*?>",' ', line)
         print match
           
strip('index.html')
 
