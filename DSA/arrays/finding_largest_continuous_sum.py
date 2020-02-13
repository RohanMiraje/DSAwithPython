def find_largest_continuous_sum(input_arr):
    """
    This solution uses aux space
    TC: O(n)+O(nLogn) ==>O(nLogn)
    SC: O(n)
    :param input_arr:
    :return:
    """
    prefix_sum_array = list()
    prefix_sum = 0
    for val in input_arr:
        prefix_sum += val
        prefix_sum_array.append(prefix_sum)
    prefix_sum_array.sort()
    print(prefix_sum_array[-1])


def find_max(input_arr):
    """
    This is better approach
    TC: O(n)
    SC:O(1)
    Idea is to decide max of curr_sum and curr_ele while traversing array
        For curr_sum add curr_ele to it and compare with curr_ele
        then update curr_sum as max of this comparison
    :param input_arr:
    :return:
    """
    curr_max = max_sum = input_arr[0]
    i = 1
    while i < len(input_arr):
        curr_max = max(curr_max + input_arr[i], input_arr[i])
        if curr_max >= max_sum:
            max_sum = curr_max
        i += 1
    print(max_sum)


if __name__ == '__main__':
    find_largest_continuous_sum([1, 2, -1, 3, 4, 10, 10, -10, 1])
    find_max([1, 2, -1, 3, 4, 10, 10, -10, 1])
