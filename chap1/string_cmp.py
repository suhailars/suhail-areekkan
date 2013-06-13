import sys
def cmp(s,b):
  t=0
  if len(s) != len(b):
    print False
  else: 
    for i in s:
      if i != b[t]:
         flag=1
      else: flag=0
      t=t+1
    if flag==1:
      print False
    else:
      print True
cmp(sys.argv[1],sys.argv[2])
