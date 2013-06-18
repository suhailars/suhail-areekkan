import os
import sys
def findfiles(dir1):
     for root,dirs,files in os.walk('suh'):
         #print root
         #print dirs
        # print files
         d=os.path.basename(root) 
         for f in files:
               yield (os.path.abspath(os.path.join(f)))  
         if d==dir1:
                sys.exit(1) 
                
def main(dir1):
    lines = findfiles(dir1)                  
    for line in lines:
         print line                    
main('vijay')            
