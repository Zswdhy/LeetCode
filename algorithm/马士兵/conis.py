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
            res = min(res, subproblem + 1)  # 符合条件每次 + 1

        return res if res != float('INF') else -1

    return dp(amount)


if __name__ == '__main__':
    coins = [1, 2, 5]
    amount = 11

    a = coinChange(coins, amount)
    print(a)
