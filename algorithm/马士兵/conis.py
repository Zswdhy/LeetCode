def coinChange(coins, amount):
    def dp(n):
        if n < 0:
            return -1
        if n == 0:
            return 0
        res = float('INF')
        for coin in coins:
            subproblem = dp(n - coin)
            if subproblem == -1:
                continue
            # 状态转移方程，求最小值
            res = min(res, subproblem + 1)  # 符合条件每次 + 1，求最小值

        return res if res != float('INF') else -1

    return dp(amount)


def process(weights, values, index, curWeight, bag):
    """
    :param weights: 重量列表
    :param values:  价值列表
    :param index:   当前索引值
    :param curWeight:   当前重量
    :param bag:         背包重量
    :return: 最大值
    """
    # 超过背包重量
    if curWeight > bag:
        return -1
    # 当前 index 达到最大值
    if index == len(weights):
        return 0

    # 忽略本次的重量以及价值
    p1 = process(weights, values, index + 1, curWeight, bag)

    # 计算本次的重量以及价值
    p2Next = process(weights, values, index + 1, curWeight + weights[index], bag)
    p2 = -1
    if p2Next != -1:
        p2 = p2Next + values[index]
    # 状态转移方程，求最大值
    return max(p1, p2)


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11

    a = coinChange(coins, amount)
    print(a)

    weights = [5, 4, 3, 14, 12, 9, 4, 3]
    values = [3, 4, 5, 10, 9, 8, 2, 1]
    bag = 30
    res = process(weights, values, 0, 0, bag)
    print('max values', res)
