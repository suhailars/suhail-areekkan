import os
def findfile(dir1):
     for root,dirs,files in os.walk('suh'):
         
         match=os.path.basename(root)
         if match==dir1:
          for f in files:
               if f in '.py':
  		  for lines in open(f):
                        yield lines

def findpython(lines):
       return (lines for lines in open(f) if '.py' in f)
def printfiles(lines):
         c=0
         for lines in open(f):
              c=c+1
         print c   
           
def main(dir1):
     lines = findfile(dir1)
     lines = findpython(lines)
     printfiles(files)
main('vijay')
