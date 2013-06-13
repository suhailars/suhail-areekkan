def rev(a):
    l=[]
    for i in a:
     l.insert(0,i)
    #print l
    return l
a=[1,2,3,4]
print a
print rev(rev(a))
