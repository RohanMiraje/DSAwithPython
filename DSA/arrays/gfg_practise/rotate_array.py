def rotate_array(arr, n, k):
    rotate_by_block = gcd(n, k)
    print(rotate_by_block)
    for i in range(rotate_by_block):
        j = i
        temp = array[i]
        while True:
            s = (j + k) % n
            if s == i:
                break
            arr[j] = arr[s]
            j = s
        arr[j] = temp


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


if __name__ == '__main__':
    # array = [1, 2, 3, 4, 5]
    # rotate_array(array, len(array), 2)
    # print(array)
    t = int(input())
    for _ in range(t):
        n, pos = tuple(map(int, input().split()))
        array = list(map(int, input().split()))
        rotate_array(array, len(array), 2)

