def myAtoi(s):
    s = s.strip()
    print('s', s, s[0], s[0].isdecimal())
    if s[0] not in ['-', '+'] or not s[0].isdecimal():
        print('11112')
        return 0
    res = ""
    for item in s:
        print('item', item)
        if item in ['-', '+'] or item.isdecimal():
            res += item

    return res


if __name__ == '__main__':
    s = '   4193 with words'
    print('原始字符串', s)
    res = myAtoi(s)
    print('res', res)
