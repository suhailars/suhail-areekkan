def flatlist(list1):
             ind=0 
             for i in list1:
               if isinstance(i,list):
                   flatlist(i)
               else :
                   ind=list1.index(i)
                   i=function(i)
                   list1.insert(ind,i)      
             return list1     
def function(i):
     return i*i

print flatlist([[1, 2], [3, [4, 5]], 6]) 
