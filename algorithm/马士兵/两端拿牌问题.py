"""
给定一个整型数组 arr ， 代表数值不同的纸牌拍成一条线
玩家 A 和玩家 B 依次拿走每张纸牌
规定玩家 A 先拿，玩家 B 后拿
但是每个玩家每次只能拿走最左或最右的纸牌
返回胜利者的分数
"""


# 先手，考虑对自己有利的的拿牌顺序
def first(arr, left, right):
    if left == right:
        return arr[left]
    # 返回最大的值
    return max(arr[left] + second(arr, left + 1, right),
               arr[right] + second(arr, left, right - 1))


# 后手，对手拿走最有利的牌
def second(arr, left, right):
    if left == right:
        return 0
    # 返回最小的值
    return min(first(arr, left + 1, right),
               first(arr, left, right - 1))


def win(arr):
    if not arr or len(arr) == 0:
        return 0
    return max(first(arr, 0, len(arr) - 1), second(arr, 0, len(arr) - 1))


if __name__ == '__main__':
    arr = [1, 100, 1]
    res = win(arr)
    print(res)
