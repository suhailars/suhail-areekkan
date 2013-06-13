def product(a):
    sum=1
    for i in a:
      sum=sum*i
    print sum
#print product([1,2,3])
def fact(a):
    l=[]
    while(a>0):
      l.append(a)
      a-=1
    print 'fact is:',product(l)
fact(4)

