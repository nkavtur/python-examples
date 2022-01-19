def zigzag_array(array):

    flag = True


    for i in range(len(array) - 1):

        if array[i] > array[i + 1] and flag:
            array[i], array[i + 1] = array[i + 1], array[i]
        elif array[i] < array[i + 1] and not flag:
            array[i], array[i + 1] = array[i + 1], array[i]

        flag = not flag

    return array


# a < b > c < d > e < f
print(zigzag_array([4, 3, 7, 8, 6, 2, 1]))
print(zigzag_array([1, 4, 3, 2]))
