def invert1(d):
    l={}
    print d
    for key in d.keys():
         l[d[key]]=key
    print l
invert1({'x': 1,'y': 2,'z': 3})     
