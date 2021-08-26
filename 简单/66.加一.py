def plusOne(digits: list) -> list:
    old_str = "".join([str(item) for item in digits])
    new_num = int(old_str) + 1
    return [int(item) for item in list(str(new_num))]


def plusOne2(digits: list) -> list:
    """
    只需要对于数字为 9 进行特殊处理即可
    :param digits:
    :return:
    """
    digits[-1] += 1
    # 逆序循环
    for i in range(len(digits) - 1, -1, -1):
        # 如果当前的数字为 10
        if digits[i] == 10:
            # 更新当前位置的值
            digits[i] = 0
            # 第一位
            if i == 0:
                digits = [1] + digits
            # 其余位置
            else:
                digits[i - 1] += 1

    return digits


if __name__ == '__main__':
    digits = [9, 9, 9]
    res = plusOne(digits)
    res2 = plusOne2(digits)
