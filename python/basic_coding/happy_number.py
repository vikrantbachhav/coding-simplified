# For a happy number, sum of square of each number lead to 1

def is_happy_number(n):
    slow, fast = n, n

    while True:
        slow = get_next_value(slow)
        fast = get_next_value(get_next_value(fast))
        print(slow, fast)
        if slow == fast:
            break
    return slow == 1


def get_next_value(n):
    square = 0

    while n > 0:
        t = n % 10
        square += t * t
        n = n // 10

    return square


if __name__ == '__main__':
    print(is_happy_number(19))
    print(is_happy_number(25))
