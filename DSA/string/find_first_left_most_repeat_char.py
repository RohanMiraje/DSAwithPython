"""
find first repeat char's leftmost index in given string text
"""


def left_most_index(string):
    first_index = [-1 for _ in range(256)]
    for i, letter in enumerate(string):
        ascii_index = ord(letter)
        if first_index[ascii_index] == -1:
            first_index[ascii_index] = i
        elif first_index[ascii_index] != -1:
            return first_index[ascii_index]
    return None


if __name__ == '__main__':
    text = "abcdabcd"
    print(left_most_index(text))
