from arrays.template import *


def create_array(n):
    global prefix_sum_array
    input_arr = get_sequence_list(n)
    prefix_sum_array = create_prefix_sum_array(input_arr)


def give_sum(start_index, end_index):
    if start_index == 0:
        return prefix_sum_array[end_index]
    return prefix_sum_array[end_index] - prefix_sum_array[start_index - 1]


if __name__ == '__main__':
    create_array(10)
    print(give_sum(1, 4))
