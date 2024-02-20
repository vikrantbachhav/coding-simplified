# recursive solution
def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)

#for loop
def factorial(n):
    fac = 1
    for i in range(1, n+1):
        fac = fac * i
    return fac

n = 5
print(fact(n))
print(factorial(5))