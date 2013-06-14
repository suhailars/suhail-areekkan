import re
def regular():
    k=0 
    i=""
    
    while(k<10):
     if k != 9:
      i+='\d'
     else:
       i+='\d'
     k+=1  
    print 'regular exp is:',i
    return i
def phone():
     print 'entr a phone no'
     s=raw_input()
     match=re.search(regular(),s)
     if match:
          print 'good phone no tc!'
     else: print 'bad!not a no' 
     
phone() 

