"""
子序列：顺序可以不连续，但是顺序不可以改变
"""


def child_sequence(s, index, ans, path):
    """
    :param s:原始字符串【list】
    :param index: 当前索引位置
    :param ans: 最终返回子序列
    :param path: 每次遍历到的原色
    :return: ans
    """
    if index == len(s):
        if path not in ans:
            ans.append(path)
    else:
        choice_no = path  # 不选择当前元素,无须修改之前路径位置
        child_sequence(s, index + 1, ans, choice_no)
        choice_yes = path + s[index]  # 选择当前元素，修改当前路径
        child_sequence(s, index + 1, ans, choice_yes)
    return ans


if __name__ == '__main__':
    s = 'aaaa'
    s = list(s)
    path = ""
    ans = []
    res = child_sequence(s, 0, ans, path)
    print('马士兵', res)
