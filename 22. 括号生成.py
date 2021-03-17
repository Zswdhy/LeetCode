# 深度优先遍历【使用系统栈】   回溯 + 剪枝
def generateParenthesis(n):
    res = []
    cur_str = ''

    def func(cur_str, left, right):
        """
        :param cur_str: 目前符合情况的排列
        :param left: 左括号剩下的使用次数
        :param right: 右括号剩下的使用次数
        :return:
        """
        if left == 0 and right == 0:
            res.append(cur_str)
            return
        # 剪枝操作，当 r < l 不满足匹配情况【当前状态的 右括号数量 > 左括号数量】
        if right < left:
            return
        if left > 0:
            func(cur_str + '[', left - 1, right)
        if right > 0:
            func(cur_str + ']', left, right - 1)

    func(cur_str, n, n)
    return res


if __name__ == '__main__':
    n = 3
    res = generateParenthesis(n)
    print(res)
