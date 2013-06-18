def iterzip(list1,list2):
    d={}
    k=0
    for i in list1:
      d[i] = list2[k]
      k+=1
    for k in sorted(d.keys()):
     print k,' ',d[k]
iterzip(['a','b','c'],[1,2,3])

