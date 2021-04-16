"""
    任意的两个皇后不共行、共列、共对角【正、反】
    时间复杂度：均为 n**n
"""


def isValid(record, i, j):
    for k in range(i):
        if j == record[k] or abs(record[k] - j) == abs(i - k):
            return False
    return True


def process(recode, i, n):
    """
    :param i: 当前行数
    :param recode: 用于存储当前符合条件的列数
    :param n: 总行数
    :return: 符合的次数
    """
    # 终止，返回一种
    if i == n:
        return 1
    # 其他情况
    res = 0
    for j in range(n):
        # 计算 i行 j列 是否符合条件约束
        if isValid(recode, i, j):
            # 记录i行 j列的位置
            if len(recode) == 0 or i >= len(recode):
                recode.append(j)
            else:
                recode[i] = j
            res += process(recode, i + 1, n)
    return res


def num2(n):
    # 非正常数字
    if n < 1 or n > 32:
        return 0
    if n == 32:
        limit = -1
    else:
        # 初始化二进制数，n为N皇后中的N
        limit = (1 << n) - 1
    return process_2(limit, 0, 0, 0)


def process_2(limit, colLimit, leftLimit, rightLimit):
    """
    :param limit: 初始位置 N个1
    :param colLimit: 列 限制
    :param leftLimit: 左对角线 限制
    :param rightLimit: 右对角线 限制
    :return:
    """
    # 满足N皇后限制
    if colLimit == limit:
        return 1

    # colLimit | leftLimit | rightLimit 当前状态下 1 不能填值的位置
    # ~(colLimit | leftLimit | rightLimit)  状态为 1 可以填值
    # pos 状态为 0 可以填值 【恢复原始的长度，左移时可能长度增长】
    pos = limit & (~(colLimit | leftLimit | rightLimit))
    # mostRightOne = 0
    res = 0
    while pos != 0:
        # 提取最右边的 1
        mostRightOne = pos & (~pos + 1)
        # 更新 pos 便于提取下一次最右侧的 1
        pos = pos - mostRightOne
        res += process_2(limit, colLimit | mostRightOne, (leftLimit | mostRightOne) << 1,
                         (rightLimit | mostRightOne) >> 1)

    return res


if __name__ == '__main__':
    import time

    n = 12
    start2 = time.time()
    details_2 = num2(n)
    print('位运算解法', details_2)
    end2 = time.time()
    print('func2', end2 - start2)

    start1 = time.time()
    details = process([], 0, n)
    print('暴力解法', details)
    end1 = time.time()
    print('func1', end1 - start1)
