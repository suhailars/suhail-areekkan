def product(a,b):
            if a==0:
             return 0
            else:
              return b+product(a-1,b)
print product(100,100) 
