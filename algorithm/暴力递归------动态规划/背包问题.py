"""
给定两个长度都为 N 的数据 weights 和 values
weights[i] 和 values[i] 分别代表 i 号物品的重量和价值
给定一个正数 bag ，表示一个载重 bag 的袋子
你装的物品不能超过这个重量
返回你能装下最多的价值是多少
"""


def process(weights, values, index, alreadyw, bag):
    """
    :param weights: 货物重量 list
    :param values: 货物价值 list
    :param index: 索引
    :param alreadyw: 当前货物的重量
    :param bag: 背包总重量
    :return: 价格
    """
    # 超重
    if alreadyw > bag:
        return -1
    # 未超重
    if index == len(weights):
        return 0
    # 未接受当前索引为 index 的货物, 因此 alreadyw 值无须改变
    p1 = process(weights, values, index + 1, alreadyw, bag)

    # 接受当前索引为 index 的货物，因此 alreadyw + weights[index]
    p2next = process(weights, values, index + 1, alreadyw + weights[index], bag)
    p2 = -1
    if p2next != -1:
        p2 = values[index] + p2next
    return max(p1, p2)


def process_2(weights, values, index, rest):
    """
    :param weights:
    :param values:
    :param index:
    :param rest: 当前情况下 bag 剩余的空间【重量】
    :return:
    """

    if rest < 0:
        return 0
    if index == len(weights):
        return 0
    p1 = process_2(weights, values, index + 1, rest)
    p2 = 0
    if rest >= weights[index]:
        p2 = values[index] + process_2(weights, values, index + 1, rest - weights[index])

    return max(p1, p2)


if __name__ == '__main__':
    weights = [5, 4, 3, 14, 12, 9, 4, 3]
    values = [3, 4, 5, 10, 9, 8, 2, 1]
    bag = 30
    res = process(weights, values, 0, 0, bag)

    res_2 = process_2(weights, values, 0, bag)
    print(res)

    print(res_2)
