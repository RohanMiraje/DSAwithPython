from arrays.template import *


def find_sub_array_with_given_sum(arr, sub_array_sum):
    prefix_array = create_prefix_sum_array(arr)
    i = 0
    j = len(prefix_array) - 1
    if sub_array_sum == prefix_array[0]:
        return True
    elif sub_array_sum == prefix_array[len(prefix_array) - 1]:
        return True
    elif sub_array_sum > prefix_array[len(prefix_array)-1]:
        return False
    while i <= j:
        if prefix_array[j] == sub_array_sum:
            return True
        elif prefix_array[j] < sub_array_sum:
            j += 1
            while i < j:
                if prefix_array[j] - prefix_array[i] == sub_array_sum:
                    return True
                i += 1
            return False
        j -= 1
    return False


def find_max_sum_of_k_elements(arr, k):
    max_sum = sum(arr[0:k])
    i = 1
    while i <= len(arr) - k:
        new_sum = max_sum - arr[i - 1] + arr[i + k - 1]
        if max_sum < new_sum:
            max_sum = new_sum
        i += 1
    print("max_sum:{} from index:{} to {}".format(max_sum, i - 1, i + k - 2))


if __name__ == '__main__':
    sum_of_sub_array = 15
    input_list = get_sequence_list(10)
    print("is present:{}".format(find_sub_array_with_given_sum(input_list, sum_of_sub_array)))
    # find_max_sum_of_k_elements(input_list, 3)
