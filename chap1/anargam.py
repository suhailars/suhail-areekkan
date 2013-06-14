def anarg(a):
     k=0
     l=[]
     r=[]
     v=[]
     flag=0
     for i in a:
      for j in a[k+1:]:
       if  isAnagram(i,j) :
            l.append(j)
            flag=1     
      if flag==1 :
          l.append(i)
          r.append(l)
          flag=0
          l=[]   
      k+=1          
     print r 
def isAnagram(str1, str2):
    str1_list=list(str1)
    str1_list.sort()
    str2_list=list(str2)
    str2_list.sort()

    return (str1_list == str2_list )
anarg(['eat','ate','fo','of','ta','at'])    


