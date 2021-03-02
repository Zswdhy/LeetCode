def reverse(x):
    def judge(a):
        if a > 2 ** 31 - 1 or a < -2 ** 31:
            return 0
        return a

    x = str(x)
    if len(x) == 1:
        return int(x)
    if x[0] == '-':
        temp = x[1::]
        res = int(x[0] + temp[::-1])
        return judge(res)
    res = int(x[::-1])
    return judge(res)


if __name__ == '__main__':
    x = 1534236469
    print('原始', x)
    res = reverse(x)
    print('反转', res)
