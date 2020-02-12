def are_anagrams(str1, str2):
    str1 = str1.replace(' ', '')
    str2 = str2.replace(' ', '')
    n1 = len(str1)
    n2 = len(str2)
    if n1 != n2:
        return False
    res = ord(str1[0])
    for i in range(1, n1, 1):
        res ^= ord(str1[i])
    print(res)
    res2 = ord(str2[0])
    for i in range(1, n1, 1):
        res2 ^= ord(str2[i])
    print(res2)
    return res ^ res2 == 0


if __name__ == '__main__':
    s1 = "rohan mukund miraje"
    s2 = "miraje rohan mukund"
    """
    Using XOR operations on ascii values of chars of both string ....last result should be zero 
    """
    print(are_anagrams(s1, s2))
