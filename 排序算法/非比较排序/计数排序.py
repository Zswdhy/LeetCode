"""
    计数排序：适用于k不是很大，并且比较集中的情况.
    时间复杂度：O(n+k)
    空间复杂度：O(n+k)
    【注】:n代表数组长度，k代表数组内有k个不同的数字
    空间换时间的排序算法.
"""


def count_sort(ls):
    min, max = ls[0], ls[0]
    for item in ls:
        if item < min:
            min = item
        elif item > max:
            max = item

    res = [0 for i in range(min, max + 1)]

    for item in ls:
        res[item - min] += 1
    fin_res = []
    for i in range(len(res)):
        for j in range(res[i]):
            fin_res.append(i + min)
    return fin_res


if __name__ == '__main__':
    ls = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    res = count_sort(ls)
    print("排序结果:", res)
