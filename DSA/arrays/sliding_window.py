from arrays.input_header import input_array, input_list


def find_max_sum_of_k_consecutive_elements(arr, window_size):
    print("i/p arr{}".format(arr))
    max_sum = 0
    i = 0
    while i < len(arr):
        sum_of_k = sum(arr[i:window_size+i])
        if sum_of_k > max_sum:
            max_sum = sum_of_k
        i += 1
    print(max_sum)


if __name__ == '__main__':
    find_max_sum_of_k_consecutive_elements(input_list, 3)
