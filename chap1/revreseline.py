def rev(filename):
     l=[]
     f=open(filename,'r')
     l=f.readlines()
     print l
     for i in l[::-1]:
      if i !='\n':
       print i
       
     f.close()
rev('suh.txt')
