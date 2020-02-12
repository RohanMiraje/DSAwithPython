import sys


def find_kth_smallest(array, k):
    n = len(array)
    if k > n:
        print("invalid inputs k:{} n:{}".format(k, n))
        return
    kth_smallest = array[0]
    i = 1
    while i < n:
        print("I+1:{}".format(i + 1))
        if i + 1 % k == 0:
            if kth_smallest > array[i]:
                kth_smallest = array[i]
        i += 1
    return kth_smallest


if __name__ == '__main__':
    print(find_kth_smallest([5, 4, 3, 1], 2))
