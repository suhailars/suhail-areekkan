def head(filename):
     f=open(filename,'r')
     t=f.readlines()
     print "head:"
     for i in t[:10]:
       print i[:-1] 
def tail(filename):
     f=open(filename,'r')
     t=f.readlines()
     print "tail:"
     for i in t[-10:]:
      print i[:-1]
head('suh.txt')
tail('suh.txt')
