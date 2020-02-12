"""
find first non-repeat char's leftmost index in given string text
"""


def left_most_index_non_repeat(string):
    first_index = [-1 for _ in range(256)]
    for i, letter in enumerate(string):
        ascii_index = ord(letter)
        if first_index[ascii_index] == -1:
            first_index[ascii_index] = i
        elif first_index[ascii_index] != -1:
            first_index[ascii_index] = -2
    for i, val in enumerate(first_index):
        if val != -2 and val != -1:
            return val
    return - 1



if __name__ == '__main__':
    text = "abcdjjkabcd"
    print(left_most_index_non_repeat(text))
