def myAtoi(s):
    s = s.strip()
    import re
    res = re.match('[+|-]{0,1}\d+', s)
    if res:
        temp = res.group()
        if int(temp) < -2 ** 31:
            return -2 ** 31
        elif int(temp) > 2 ** 31 - 1:
            return 2 ** 31 - 1
        else:
            return int(temp)
    else:
        return 0


if __name__ == '__main__':
    s = '   4193 with words'
    res = myAtoi(s)
    print('res', res)
