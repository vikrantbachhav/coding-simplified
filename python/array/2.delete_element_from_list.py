# Solution: Using Python Native methods
def delete_element_from_list():
    array = []
    for j in range(0, 10):
        array.append(j)

    print(len(array), array)

    # remove element at given index
    del array[0]
    print("Given Index removal i=0", array)

    # remove first occurance of the specified value
    array.remove(1)
    print("Remove first occurance of 1", array)

    # remove all occurances of specified value
    array.append(2)
    print("Add element 2 to array", array)
    print("Remove all occurances of 2", [x for x in array if x!= 2])

    # remove all occurances of specified value
    array.append(3)
    print("Add element 3 to array", array)
    print("Remove all occurances of 3", list(filter(lambda x: x != 3, array)))

    # remove all occurances of specified value
    array.append(4)
    print("Add element 4 to array", array)
    while 4 in array:
        array.remove(4)
    print("Remove all occurances of 4", array)

    array.pop()
    print(array)

    array.pop(0)
    print(array)

    array.clear()
    print(array)

# Instantiate the class and call the main method
if __name__ == "__main__":
    delete_element_from_list()