def convert(s, numRows):
    """
    仅适合于三层 Z 字型，其他的存在 Bug
    :param s:
    :param numRows:
    :return:
    """
    l = len(s)
    col = (l // (numRows + numRows - 2)) * (numRows - 1) + 1
    matrix = [[' '] * col for i in range(numRows)]
    n = 2 * numRows - 2
    for i, char in enumerate(s):
        x = i % n
        y = min(x, n - x)  # row

        if x == numRows:
            z = 2 * (i // n) + 1  # col
        else:
            z = 2 * (i // n)

        matrix[y][z] = char

    res = ''
    for item in matrix:
        res += ''.join(item)
    return res.replace(" ", "")
    # return matrix


def demo(s, numRows):
    if numRows == 1:
        return s

    rows = [""] * numRows  # 初始化列表，加入到指定的行内
    n = 2 * numRows - 2
    for i, char in enumerate(s):
        x = i % n  # row
        rows[min(x, n - x)] += char  # col
    return "".join(rows)


if __name__ == '__main__':
    s = "PAYPALISHIRING"
    numRows = 4
    res = convert(s, numRows)

    # print(demo(s, numRows))
    print('res', res)
