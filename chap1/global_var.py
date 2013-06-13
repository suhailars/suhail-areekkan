num=0
def square(x):
    global num
    num = num + 1
    return x * x
print square(2),num  
