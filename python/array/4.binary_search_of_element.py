def binary_search_element_rec(array, element, start, end):

    if start > end:
        return False

    mid = (start + end) // 2
    print(mid, array[mid])
    if array[mid] == element:
        return True
    elif array[mid] < element:
        return binary_search_element_rec(array, element, mid + 1, end)
    else:
        return binary_search_element_rec(array, element, start, mid - 1)

def binary_search_element(array, element, start, end):

    if start > end:
        return False

    while start <= end:
        mid = (start + end) // 2
        print(mid, array[mid])
        if array[mid] == element:
            return True
        elif array[mid] < element:
            start =  mid + 1
        else:
            end = mid - 1
    return False

if __name__ == '__main__':
    array = [12, 34, 45, 65, 83]
    element = 83

    start = 0
    end = len(array)-1
    print(array)

print(binary_search_element_rec(array, element, start, end))
print(binary_search_element(array, element, start, end))