def rotate_array_left_by_one(input_array):
    temp = input_array[0]
    for index, val in enumerate(input_array):
        if index == len(input_array) - 1:
            break
        input_array[index] = input_array[index + 1]
    input_array[-1] = temp


"""
e.g input_array = [1,2,3,4,5,6,7], k = 2
output = [3,4,5,6,7,1,2]
"""


def rotate_array_left_by_k_positions(arr, k):
    if k <= 0:
        return
    print("rotate_array_left_by_{}_positions".format(k))
    for i in range(k):
        rotate_array_left_by_one(arr)
    print(arr)


"""
e.g input_array = [1,2,3,4,5,6,7], k = 2
output = [7,6,1,2,3,4,5]
"""


def rotate_array_clockwise_by_k_positions(arr, k):
    if k <= 0:
        return
    print("rotate_array_clockwise_by_{}_positions".format(k))
    for i in range(k):
        temp = arr[-1]
        for index in range(-1, -len(arr), -1):
            arr[index] = arr[index - 1]
        arr[0] = temp
    print(arr)


def reversal_array_algorithm(arr, k):
    rotate_array(arr, 0, k - 1)
    rotate_array(arr, k, len(arr) - 1)
    rotate_array(arr, 0, len(arr) - 1)
    print(arr)


def rotate_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


if __name__ == '__main__':
    array = [i for i in range(1, 8)]
    print("Input array:{}".format(array))
    # import copy
    #
    # test_arr = copy.deepcopy(array)
    # rotate_array_left_by_k_positions(test_arr, 2)
    # test_arr = copy.deepcopy(array)
    # rotate_array_clockwise_by_k_positions(test_arr, 2)
    reversal_array_algorithm(array, 2)
