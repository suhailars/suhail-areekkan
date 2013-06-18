import re
import urllib2
import os
import sys
"""def urldown(url):
     file= urllib2.urlopen(url)
     s=os.path.basename(url)
     if s=='':
        filename='index.html'
     else: 
        filename=s
     f=open(filename,'w')
     for line in file:
      f.write(line)
     f.close()
     return filename """
def url_link(filename):
    # filename=urldown(sys.argv[1]) 
     f=open(filename,'r')
     s=f.read()
     match=re.findall(r'(http://\S+)"',s)
     for i in  match:
      print i
url_link('index.html')
