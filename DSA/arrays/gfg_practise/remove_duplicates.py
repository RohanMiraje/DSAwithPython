def remove_duplicates(arr):
    for val in arr:
        if arr[abs(val)] > 0:
            arr[abs(val)] = - arr[abs(val)]
    aux = []
    for val in array:
        if val < 0:
            aux.append(val)
    print(aux)


if __name__ == '__main__':
    array = [1, 2, 3, 1, 4, 2]
    remove_duplicates(array)
    # t = int(input())
    # for _ in range(t):
    #     n = int(input())
    #     array = list(map(int, input().split()))
    #     remove_duplicates(array)
    #     for i in array:
    #         print(i, end=" ")
    #     print('')
