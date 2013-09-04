import os
import sys 
def dirtree(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}'.format(indent, os.path.basename(root)))
        l=1
        if level==0:
          subindent=' '*(len(root)-1)+'|...'
        else:
          subindent = 2*indent+'' * 4 * (level + 1)+'|...'
        for f in files:
            print('{}{}'.format(subindent, f))     
dirtree(sys.argv[1])
 
