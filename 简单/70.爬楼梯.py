def climbStairs(n: int) -> int:
    """
    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
    每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    递归
    :param n:
    :return:
    """
    if n == 1 or n == 2:
        return n
    return climbStairs(n - 1) + climbStairs(n - 2)


def climbStairsPlus(n: int) -> int:
    """
    动态规划方程：f(x) = f(x-1) + f(x-2)
    假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
    每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
    :param n:
    :return:
    """
    # p:第一个状态
    # q:第二个状态
    p, q, r = 0, 0, 1
    for i in range(n):
        p = q
        q = r
        r = p + q
    return r


if __name__ == '__main__':
    n = 3
    res = climbStairs(n)
    print(res)
