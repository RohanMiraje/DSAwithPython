"""
[1,1,1,5,3,5,5,5,3]
n = 9
o/p: major_elem is more than n//2

expected TC->O(n), SC:O(1) ---> use moore voting algorithm
"""


def find_majority(array):
    """
    This solution works in nlogn time
    :param array:
    :return:
    """
    n = len(array)
    i = 0
    array = sorted(array)  # nlogn
    majority = -1
    while i < n:  # n
        majority = find_no_of_occurrence_of_key(array, 0, n, array[i])  # logn
        if majority >= n // 2:
            break
        i += 1
    return array[i] if majority != -1 and i != n else -1


def find_no_of_occurrence_of_key(arr, low, high, key):
    left_most_index = find_left_most_index(arr, low, high, key)
    if left_most_index == -1:
        return -1
    right_most_index = find_right_most_index(arr, low, high, key)
    return right_most_index - left_most_index + 1


def find_left_most_index(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key and (mid == 0 or arr[mid - 1] != key):
            return mid
        elif arr[mid] >= key:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def find_right_most_index(arr, low, high, key):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key and (mid == len(arr) - 1 or arr[mid + 1] != key):
            return mid
        elif arr[mid] <= key:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def majority(array, length):
    """
    https://www.geeksforgeeks.org/majority-element/
    :param array:
    :param length:
    :return:
    """
    count = 1
    i = 1
    major_index = 0
    while i < length:
        if arr[major_index] == array[i]:
            count += 1
        else:
            count -= 1
        if count == 0:
            major_index = i
            count = 1
        i += 1
    count = 1
    for val in array:
        if val == array[major_index]:
            count += 1
            pass
        if count >= length // 2:
            return array[major_index]


if __name__ == '__main__':
    # print(find_majority([1, 1, 1, 5, 3, 5, 5, 5, 3, 5]))
    # size = 20
    # arr = [-1] * 20
    # for i in [1, 1, 1, 5, 3, 5, 5, 5, 3, 5]:
    #     arr[]
    # arr = [1, 1, 1, 5, 3, 5, 5, 5, 3, 5]
    arr = [1, 1, 1, 1, 1, 1, 1, 1, 5, 5, 5, 5, 5]
    size = len(arr)
    print(majority(arr, size))
