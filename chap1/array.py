#import sys 
def array(a,b):
    l=[]
    l=[[None]*b for i in range(a)]
    print l
    return l
def addarray(raw,colum,n):
   
    l=[]
    l=array(2,3)
    l[raw][colum]=n
    #l.insert(0,0,'1')
    print l
              
array(2,3)
addarray(0,0,1) 
