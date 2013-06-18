import  tablib
import re
def createcsv(filename):
    data = tablib.Dataset()
    data.append(['A',1 ]) 
    data.append(['B',2])
    data.append(['c',3])
    with open(filename,'wb') as f:
         f.write(data.csv)
    f.close()
    xlxs(filename)
def xlxs(filename):
    data1= tablib.Dataset()
    f=open(filename,'r')
    t=f.readlines() 
    for line in t:
      mt=re.search(r'(\w+),(\w+)',line)
      data1.append ([mt.group(1),mt.group(2)])
    f.close()
    match=re.search(r'\w+',filename)
    t=match.group()+'.xlsx'
    print t
    with open(t,'wb') as f:
        f.write(data1.xlsx)
    f.close() 
    return True
createcsv('test.csv')
