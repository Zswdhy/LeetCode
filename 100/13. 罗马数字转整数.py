def romanToInt(s):
    d = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50, 'XC': 90, 'C': 100, 'CD': 400, 'D': 500,
         'CM': 900, 'M': 1000}
    res = 0
    i = 0
    # key 最长长度为 2 因此每次取 2 长度，存在，则转换
    # 否则，取 1 长度，进行转化
    while i < len(s):
        if s[i:i + 2] in d:
            res += d[s[i:i + 2]]
            i += 2
        else:
            res += d[s[i]]
            i += 1
    return res


if __name__ == '__main__':
    s = 'LVIII'

    res = romanToInt(s)
    print('res', res)
