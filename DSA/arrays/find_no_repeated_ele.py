def find_non_repeated_in_array(array):
    """
    assuming sorted array
    Given array has elements repeated thrice but only element is non repeated
    find non repeated
    else if not print -1
    Input
        a = [1, 1, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
    output = 2 --->non repeated
    :param array:
    :return:
    method1:
            using curr element and its second next ele to compare and check if they matches
            keep traversing from i to n
                if i < n-2 and arr[i] != arr[i+2]:
                    found
                i += 3

    """
    n = len(array)
    if n < 3:
        print("invalid input, please check once again with more than or equal to 3 elements")
        return
    i = 0
    while i < n:
        if i < n - 2 and array[i] != array[i + 2]:
            print("non repeated:{}".format(array[i]))
            break
        print("i:{}".format(i))
        i += 3
    else:
        repeated = -1 if array[n - 3] == array[n - 1] else array[n - 1]
        print("non repeated:{}".format(repeated))
    print("i:{}".format(i))


def find_non_repeated_unsorted(array):
    i = 0
    n = len(array)
    sum_with_repeated_marked = 0
    while i < n:
        if array[abs(array[i])] >= 0:
            sum_with_repeated_marked = sum_with_repeated_marked + abs(array[i]) * 3
            array[abs(array[i])] *= -1
        i += 1
    print(sum_with_repeated_marked)
    print(array)
    for i in range(len(array)):
        if array[i] < 0:
            array[i] = -1 * array[i]
        sum_with_repeated_marked = sum_with_repeated_marked - array[i]
    print(sum_with_repeated_marked)
    print("Non repeated:{}".format(sum_with_repeated_marked >> 1))


def pythonist_solution(array):
    repeated_sum = sum(set(array)) * 3
    normal_sum = sum(array)
    print("non_repeated:{}".format((repeated_sum-normal_sum) >> 1))


if __name__ == '__main__':
    # a = [2, 2, 3, 2]
    a = [0, 1, 0, 1, 0, 1, 99]
    nums = [0 for _ in range(max(a)+1)]
    for i in range(len(a)):
        nums[i] = a[i]
    # a = [1, 1, 1, 2, 3, 3, 3, 4, 4, 4, 5, 5, 5]
    # a = [1, 1, 1, 2, 2, 2, 4]
    # a = [1, 3, 3, 3]
    # find_non_repeated_in_array(a)

    find_non_repeated_unsorted(nums)
    # pythonist_solution(a)
    # print(max(a))