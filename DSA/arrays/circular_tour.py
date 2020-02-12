def get_index_of_circular_tour(array, n):
    distance_and_petrol_difference = []
    sum_ = 0
    for i in range(n):
        distance_and_petrol_difference.append(array[i][0] - array[i][1])
        sum_ += distance_and_petrol_difference[-1]
    if sum_ < 0:
        return -1
    start_point = 0
    sum_ = 0
    for i in range(n):
        sum_ += distance_and_petrol_difference[i]
        if sum_ < 0:
            start_point = i + 1
            sum_ = 0
    return start_point


if __name__ == '__main__':
    a = [[4, 6], [6, 5], [7, 3], [4, 5]]
    # a = [[96, 25], [46, 83], [68, 15], [65, 35], [51, 44], [9, 88], [79, 77], [85, 89]]
    print(get_index_of_circular_tour(a, len(a)))
