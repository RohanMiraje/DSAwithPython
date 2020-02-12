#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    prefix_sum_array = get_prefix_sum_array(arr)
    min_sum = sys.maxsize
    max_sum = -sys.maxsize
    for val in arr:
        t_min_sum = prefix_sum_array[-1] - val
        t_max_sum = prefix_sum_array[-1] - val
        if t_min_sum < min_sum:
            min_sum = t_min_sum
        if t_max_sum > max_sum:
            max_sum = t_max_sum
    print(min_sum, max_sum)


def get_prefix_sum_array(array):
    sum_array = list()
    sum_var = 0
    for i in array:
        sum_var += i
        sum_array.append(sum_var)
    return sum_array


if __name__ == '__main__':
    """
    https://www.hackerrank.com/challenges/mini-max-sum/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
    One approach could be find max and min from array and array ele sum...and then max_sum = array_sum - min_ele and min_sum = array_sum - max_ele
    other approach to use prefix sum array
    """
    arr = list(map(int, input().rstrip().split()))
    miniMaxSum(arr)
