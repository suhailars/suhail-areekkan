import sys
def enum(list1):
    d={}
    k=0
    for i in list1:
      d[k]=i
      k+=1
    
    for k,v in d.items():
     print k,' ',v
enum(sys.argv[1]) 
