#Program to create factorial of a program recursion

def fact(num):
    if num==1:
        return 1
    else:
        return num*fact(num-1)
        
        
        
print(fact(45))
