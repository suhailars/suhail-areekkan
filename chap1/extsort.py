import re
def exsort(lis):
     l=[] 
     s={}
     
     	
     for i in lis:
      match=re.search(r'(\w+)(.\w+)',i)
      print match.group(2)
      s[match.group(2)]=match.group(1)
     for key in sorted(s.keys()):
      print s[key]+key     
l=['a.txt','b.jpg','c.py','d.exe','p.rar','ab.cyj'] 
exsort(l)     
