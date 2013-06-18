def reverselist(l):
                l.reverse()
                for i in l:
                    if isinstance(i,list):
                        reverselist(i)          
                return l

print reverselist([[1, 2], [3, [4, 5]], 6])  
