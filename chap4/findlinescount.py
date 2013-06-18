import os
def findfile(dir1):
     for root,dirs,files in os.walk('suh'):
         
         match=os.path.basename(root)
         if match==dir1:
          for f in files:
               yield f

def findpython(lines):
       return (line for line in lines if '.py' in line)
def printfiles(lines):
         c=0
         for line in lines:
             path=os.path.abspath(os.path.join(line))
             print path   
           
def main(dir1):
     lines = findfile(dir1)
     lines = findpython(lines)
     printfiles(lines)
main('vijay')
