import sys 
import mutate1
def nearlyequal(st1,st2):
   if( mutate1.mutate(st1,st2)):
         print True
   else:  print False 
nearlyequal(sys.argv[1],sys.argv[2])
      
