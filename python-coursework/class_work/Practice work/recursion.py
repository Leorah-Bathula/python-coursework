#sum of N natural numbers
def display(n):
    if n == 0:
        return 0
    return n + display(n-1)    
print(display(10))


#product  of N natural numbers

def display(n):
    if n == 1:
        return 1
    return n * display(n-1)    
print(display(5))   

