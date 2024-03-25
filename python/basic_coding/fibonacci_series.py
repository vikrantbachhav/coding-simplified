# recursive solution
def fib(n):
    if n <= 1:
        return n
    else:
        return fib(n-1) + fib(n-2)

def fibo(n):
    if n <= 1:
        return n
    a,b = 0,1
    for i in range(n-1):
        c = a + b
        a = b
        b = c
    return c

# Fibonacci series - Zero indexed, starting with 0: 0,1,1,2,3,5,8,13..
print(fib(7))
print(fibo(7))