import math
def check_armstrong_num(n):
    tmp = n
    order = 0

    while(tmp > 0):
        tmp = tmp // 10
        order = order + 1

    tmp = n
    sum = 0
    for i in range(tmp - 1):
        sum = sum + math.pow(tmp % 10, order) #alternate pythonic solution is sum = sum + (tmp % 10) ** order
        tmp = tmp // 10

    return (sum == n)

if __name__ == '__main__':
    print(check_armstrong_num(153))