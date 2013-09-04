import sys
def mutate(a,b):
    flag=0
    l=[]
    if len(a)+1==len(b):
       for i in a:
         if i in b:
           flag=1  
         else :
           flag=0
           break
    elif len(a)==len(b)+1:
       for i in b:
         if i in a:
          flag=1
         else:
          flag=0
          break
    elif len(a)==len(b):
         if a==b:
            flag=1
         else:
               for i in range(len(a)-1):
                 
                  if a[i]==b[i+1] or a[i]==b[i-1]:
                           flag=1
                  
                  elif a[i]==b[i]:
                           flag=1
                  else:
                        flag=0
                        break        
    else: flag=0      
     
    if flag==1 :
       print 'found'
       return True  
    else :
       print 'not found'
       return False
print mutate(sys.argv[1],sys.argv[2]) 
