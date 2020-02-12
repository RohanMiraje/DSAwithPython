from arrays.input_header import input_array, input_list


# printing all leaders means after current element there is no other bigger element
def print_leaders(arr):
    print("i/p array:{}".format(arr))
    max_val = arr[-1]
    for i in range(-2, -len(arr) - 1, -1):
        if arr[i] > max_val:
            max_val = arr[i]
            print(max_val, end=" ")
    print(arr[-1])


if __name__ == '__main__':
    print_leaders(input_array)
