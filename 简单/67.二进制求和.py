def addBinary(a: str, b: str) -> str:
    if len(a) < len(b):
        a = "0" * (len(b) - len(a)) + a
    b = "0" * (len(a) - len(b)) + b

    l_a = len(a)
    result_str = [0 for i in range(l_a + 1)]

    for i in range(l_a - 1, -1, -1):
        if a[i] == "0" and b[i - l_a] == "0":
            result_str[i - l_a] = result_str[i - l_a]
        elif a[i] == "1" and b[i - l_a] == "1":
            result_str[i - l_a] = result_str[i - l_a]
            result_str[i - l_a - 1] = 1
        else:
            if result_str[i - l_a] == 1:
                result_str[i - l_a] = 0
                result_str[i - l_a - 1] = 1
            else:
                result_str[i - l_a] = 1

    if result_str[0] == 0:
        result_str = result_str[1:]

    return "".join([str(item) for item in result_str])


if __name__ == '__main__':
    a = "1"
    b = "111"

    res = addBinary(a, b)
    print('res', res)
