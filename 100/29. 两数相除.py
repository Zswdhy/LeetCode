def divide(dividend, divisor):
    """
    :param dividend: 被除数
    :param divisor: 除数
    :return: 商【取整】
    """
    sign = (dividend > 0) ^ (divisor > 0)  # 异或运算，两者不同时，为真
    dividend = abs(dividend)
    divisor = abs(divisor)
    count = 0

    while dividend >= divisor:  # 次数
        count += 1
        divisor <<= 1

    result = 0
    while count > 0:
        count -= 1
        divisor >>= 1
        if divisor <= dividend:
            result += 1 << count
            dividend -= divisor

    if sign:
        result = -result
    return result if -(1 << 31) <= result <= (1 << 31) - 1 else (1 << 31) - 1


if __name__ == '__main__':
    dividend = -1
    divisor = -1
    res = divide(dividend, divisor)
    print('res', res)
