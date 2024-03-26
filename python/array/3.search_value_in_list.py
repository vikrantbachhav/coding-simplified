def search_element_in_list(array, element):
    print(array)

    if len(array) == 0:
        return False
    elif element in array:
        return True

def search_element_in_list_loop(array, element):
    for i in range(len(array)-1):
        if array[i] == element:
            return True
    return False

    # for i in array:
    #     if i == element:
    #         return True
    # return False


if __name__ == '__main__':
    array = []
    element = 15
    for j in range(0, 10):
        array.append(j)

print(search_element_in_list_loop(array, element))
