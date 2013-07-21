import types
import os
import urllib2
li = ["Larry", "Curly"]
print li.pop 
print getattr(li, "pop")
print getattr(li, "append")("Moe")
print li
print  getattr({}, "clear")
try:
  print  getattr((), "pop")

except: 
 object=os
 method="listdir"  
 print type(getattr(object, method)) == types.FunctionType
 print callable(getattr(object, method))
   
