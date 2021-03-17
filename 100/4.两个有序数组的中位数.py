"""
寻找第 K 小的数字，采用二分法，每次取数据的一般进行比较

"""


def mid_num(list1, list2):
    ans = 0
    if not list1:
        l = len(list2)
        if l % 2 == 0:
            ans = (list2[l // 2] + list2[l // 2 - 1]) / 2
        else:
            ans = list2[int(l // 2)]
    if not list2:
        l = len(list1)
        if l % 2 == 0:
            ans = (list1[l // 2] + list1[l // 2 - 1]) / 2
        else:
            ans = list1[int(l // 2)]

    list1 += list2

    res = sorted(list1)
    l = len(res)
    if l % 2 == 0:
        ans = (res[l // 2] + res[l // 2 - 1]) / 2
    else:
        ans = res[int(l // 2)]

    return ans


# 第 k 小的数字
def demo(list1, list2):
    l1 = len(list1)
    l2 = len(list2)

    def min_k(k):
        n1, n2 = 0, 0

        while k != 0:
            if l1 == n1:
                return list2[n2 + k - 1]
            if l2 == n2:
                return list1[n1 + k - 1]
            if k == 1:
                return min(list1[n1], list2[n2])

            new_n1 = min(n1 + k // 2 - 1, n1 - 1)
            new_n2 = min(n2 + k // 2 - 1, n2 - 1)
            pivot_1, pivot_2 = list1[new_n1], list2[new_n2]
            if pivot_1 <= pivot_2:
                k -= (new_n1 - n1 + 1)
                n1 = new_n1 + 1
            else:
                k -= (new_n2 - n2 + 1)
                n2 = new_n2 + 1

    k = l1 + l2
    if k % 2 == 1:
        return min_k((k + 1) // 2)
    else:
        return (min_k(k // 2) + min_k((k + 2) // 2)) / 2


if __name__ == '__main__':
    list1 = [1, 3]
    list2 = [1, 2, 3]

    res = mid_num(list1, list2)
    print(res)
