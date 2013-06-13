def word_count(filename):
    f=open(filename,'r')
    t=f.read()
    l=[]
    l=t.split()
    d={}
    l2=[]
    for i in l:
     if i not in l2:
        l2.append(i) 
        count=1 
        
     else :
         count+=1
     d[i]=count
    print d
    for k in sorted(d.items(),key=myfn,reverse=True):
        print k
def myfn(d):
    return d[-1]         
           
word_count('suh.txt')
