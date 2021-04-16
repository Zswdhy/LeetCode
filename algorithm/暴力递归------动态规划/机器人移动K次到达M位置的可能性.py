"""

假设有排成一行的 N 个位置，记为 1~N , N>=2
开始时，机器人在 M 位置，M 必定在 1~N
如果机器人来到 1 位置，那么下一步只能往右来到 2 的位置
如果机器人来到 N 位置，那么下一步只能往左来到 N-1 的位置
如果机器人来到中间位置，那么下一步可以选择 左 或者 右 两个方向移动

规定机器人必须走 K 步，最总来到 P位置
"""


def ways(num, pos, k, p):
    """
    :param num: 总共的长度【可以走多少步】
    :param pos: 机器人的初始位置
    :param k: 机器人需要移动的次数
    :param p: 机器人最终来到的位置
    :return:
    """
    if num < 2 or k < 1 or pos < 1 or pos > num or p < 1 or p > num:
        return 0
    return walk(num, pos, k, p)


def walk(n, cur, rest, p):
    """
    :param n: 初试序列  固定不变
    :param cur: 当前移动到的位置
    :param rest: 剩下要走的步数
    :param p: 最总停留的位置
    :return:
    """
    # 剩余步数为 0
    if rest == 0:
        return 1 if cur == p else 0
    # 只能右移
    elif cur == 1:
        return walk(n, 2, rest - 1, p)
    # 只能左移
    elif cur == n:
        return walk(n, n - 1, rest - 1, p)

    return walk(n, cur + 1, rest - 1, p) + walk(n, cur - 1, rest - 1, p)


# 最low的动态规划 记忆搜索
def waysCache(num, pos, k, p):
    if num < 2 or k < 1 or pos < 1 or pos > num or p < 1 or p > num:
        return 0
    # 使用二维表存储每种可能
    dp = [[-1] * k for i in range(num)]
    return walkCache(num, pos, k, p, dp)


# 将所有 cur 和 rest 的组合，加入到缓存内，减少重复计算【加快速度，类似斐波那契序列】
def walkCache(n, cur, rest, p, dp):
    if dp[cur - 1][rest - 1] != -1:
        return dp[cur - 1][rest - 1]

    if rest == 0:
        dp[cur - 1][rest - 1] = 1 if cur == p else 0
        return dp[cur - 1][rest - 1]

    elif cur == 1:
        dp[cur - 1][rest - 1] = walkCache(n, 2, rest - 1, p, dp)
        return dp[cur - 1][rest - 1]
    elif cur == n:
        dp[cur - 1][rest - 1] = walkCache(n, n - 1, rest - 1, p, dp)
        return dp[cur - 1][rest - 1]

    dp[cur - 1][rest - 1] = walkCache(n, cur + 1, rest - 1, p, dp) + walkCache(n, cur - 1, rest - 1, p, dp)
    return dp[cur - 1][rest - 1]


if __name__ == '__main__':
    num = 7
    cur = 2
    k = 5
    p = 3
    print(walk(num, cur, k, p))

    print(waysCache(num, cur, k, p))
