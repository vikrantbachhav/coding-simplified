def check_palindrome(n):
    org_num = n
    s = 0
    while n > 0:
        s = s * 10 + n % 10
        n = n // 10
    return (org_num == s)

if __name__ == '__main__':
    n = 12321
    print(check_palindrome(n))