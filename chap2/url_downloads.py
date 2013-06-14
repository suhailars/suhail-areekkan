import sys
import urllib2
import os  
def dw_url(turl):
 file = urllib2.urlopen(turl)
 s=os.path.basename(turl)
 if s=='':
  filename='index.html'
 else:
  filename=s      
 f=open(filename,'w')
 for line in file: 
    f.write(line)
 f.close()
dw_url(sys.argv[1])
print 'page downloading done!!!!'

      

