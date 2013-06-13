import sys
def mutate(a,b):
    flag=0
    if len(a)<len(b):
       if b.find(a)!=-1:
          flag=1
    elif len(a)>len(b):
       if a.find(b)!=-1:
          flag=1
    elif len(a)==len(b):
         if a==b:
            flag=1
         else:
               for i in a:
                   if i in b:
                        flag=1
                   else:
                        flag=0 
                 
      
             
    else: flag=0      
     
    if flag==1 :
       print 'found'
       return True  
    else :
       print 'not found'
       return False
mutate(sys.argv[1],sys.argv[2]) 
