import sys
def centre(filename):
    f=open(filename,'r')
    text=f.readlines()
    width=[]
    
    for i in text:
      width.append(len(i))
    half=(max(width))/2
    for i in text: 	
     d=len(i)/2
     if(d<half):
         k=half-d
         while(k>0):
           i=' '+i
           k=k-1
         print i
     else :
         print i 
centre(sys.argv[1])
