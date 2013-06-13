import sys
def grep(filename):
    f=open(filename,'r')
    t=f.readlines()
    for i in t:
       if sys.argv[2] in i:
        print i
grep(sys.argv[1]) 
