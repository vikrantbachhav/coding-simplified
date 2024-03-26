# Solution: Using Python Native methods
def insert_element_in_list():
    array = []
    for j in range(0, 6):
        array.append(j)

    print(array)

    # insert element at end
    array.append(6)
    print(array)

    # insert element at given index, Ex: at start, 0th index
    array.insert(10, 9)
    for i, j in enumerate(array):
        print(i,j)


    array.insert(1, 10)
    print(array)

    array.extend([7,8,9])
    print(array)

    array += [11,12]
    print(array)

    new_elements = [13,14]
    array += new_elements
    print(array)

# Instantiate the class and call the main method
if __name__ == "__main__":
    insert_element_in_list()
