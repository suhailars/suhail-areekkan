import itertools
def permute(list1):
    l=[]  
    l=itertools.permutations(list1,len(list1))
    print list(l)
permute([1,2,3]) 
