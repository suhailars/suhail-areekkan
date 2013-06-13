def parse(filename):
   f=open(filename,'r')
   t=f.readlines()
   l=[]
   
   for v in t:
       l=v[:-1].split(',')   
       print l
       l=[]
   f.close()
parse('suh.txt') 
