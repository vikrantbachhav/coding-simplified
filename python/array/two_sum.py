"""
Given an array A[] of n numbers and another number x, the task is to check whether or not there exist two elements in A[] whose sum is exactly x.

Input: arr[] = {0, -1, 2, -3, 1}, x= -2
Output: Yes
Explanation:  If we calculate the sum of the output,1 + (-3) = -2

Input: arr[] = {1, -2, 1, 0, 5}, x = 0
Output: No

"""
# brute force solution
def two_sum(arr, size, x):
    for i in range(0, size - 1):
        for j in range(i + 1, size):
            if arr[i] + arr[j] == x:
                return True

    return False

arr = [0, -1, 2, -3, 1]
x = -2
size = len(arr)

if two_sum(arr, size, x):
    print("Yes")
else:
    print("No")
