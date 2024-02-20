# recursive solution
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

n = 5 #0,1,1,2,3,5,8,13..
print(fib(n))