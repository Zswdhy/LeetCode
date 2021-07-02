def longestValidParentheses(s):
    """
    方案一：循环遍历两次，求最大值
    :param s:
    :return: max_length
    """
    #  格式正确，且连续
    if len(s) < 2:
        return 0
    left, right, max_count = 0, 0, 0

    for item in s:
        if item == '(':
            left += 1
        else:
            right += 1
        if left == right:
            max_count = max(max_count, right * 2)
        if right > left:
            left, right = 0, 0

    left, right = 0, 0
    for item in s[::-1]:
        if item == ')':
            right += 1
        else:
            left += 1
        if left == right:
            max_count = max(max_count, left * 2)
        if right < left:
            left, right = 0, 0

    return max_count


if __name__ == '__main__':
    s = '((())'
    # s = ")()())"
    # s = "())(())"

    res = longestValidParentheses(s)

    print(f'{s}内有效括号长度为：{res}')
