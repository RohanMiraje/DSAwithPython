def find_missing_and_repeating_no_in_array(array):
    n = len(array)
    sum_n = 0
    sum_n2 = 0
    for val in array:
        sum_n += val
        sum_n2 += val * val
    x = (n * (n + 1)) // 2 - sum_n
    y = ((n * (n + 1) * (2 * n + 1)) // 6 - sum_n2) // x
    # print(sum_n, sum_n2)
    # print(x, y)
    print("repeat:{} missing:{}".format((y - x) // 2, (x + y) // 2))


def using_indexing(array):
    repeat = len(array) + 1
    for i in range(len(array)):
        if array[abs(array[i]) - 1] > 0:
            array[abs(array[i]) - 1] *= -1
        else:
            if repeat > abs(array[i]):
                repeat = abs(array[i])

    print("repeat:{}".format(repeat))

    for i in range(len(array)):
        if array[i] > 0:
            print("missing:{}".format(i + 1))
            break


if __name__ == '__main__':
    # find_missing_and_repeating_no_in_array(arr)
    # n = int(input())
    # arr = [0] * n
    # for i in range(n):
    #     arr[i] = int(input())
    # using_indexing(arr)
    using_indexing([1, 2, 2, 3, 4])
