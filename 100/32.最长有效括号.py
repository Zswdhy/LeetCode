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


def longest_valid_parent(string: str) -> int:
    max_len = -1
    stack = [-1, ]  # 防止栈为空的情况出现

    for i in range(len(string)):
        # 符合条件的左括号
        if string[i] == '(':
            stack.append(i)
        # 直接出栈操作
        else:
            stack.pop()
            # 栈不存在，将当前的索引值加入到栈内
            if not stack:
                stack.append(i)
            # 判断当前最大的 max len
            else:
                max_len = max(max_len, i - stack[-1])
    return max_len


if __name__ == '__main__':
    s = ')(()(())'
    # s = ")()())"
    # s = "())(())"

    res = longestValidParentheses(s)
    res_2 = longest_valid_parent(s)

    print(f'func 1 {s} 内有效括号长度为：{res}')
    print(f'func 2 {s} 内有效括号长度为：{res_2}')
