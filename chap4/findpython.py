import os
def findfile(dir1):
     for root,dirs,files in os.walk('suh'):
         
         match=os.path.basename(root)
         if match==dir1:
          for f in files:
               yield f

def findpython(files):
       return (f for f in files if '.py' in f)
def printfiles(files):
         for f in files:
              print f
           
def main(dir1):
     files = findfile(dir1)
     files = findpython(files)
     printfiles(files)
main('vijay')
