def find_missing_number(arr, arr2):
    complete_sum = 0
    for val in arr:
        complete_sum += val
    missing_sum = 0
    for val in arr2:
        missing_sum += val
    return complete_sum - missing_sum


def finding_missing_using_xor(arr1, arr2):
    result = 0
    for num in arr1 + arr2:
        result ^= num
    return result


if __name__ == '__main__':
    arr_1 = [1, 2, 3, 4, 5, 6, 7]
    arr_2 = [3, 7, 2, 1, 4, 6]
    print(find_missing_number(arr_1, arr_2))
    print(finding_missing_using_xor(arr_1, arr_2))
    """
    above may be problematic if arrays are two long or elements are very small
    """
    """
    other approach could be using dict-> adding no. of items in first array...and check is it in other list 
    """
    """
    exclusive or could be one more solution
    """
