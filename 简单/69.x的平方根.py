def mySqrt(x: int) -> int:
    mid_num = x // 2
    for i in range(1, mid_num + 2):
        if i * i == x:
            return i
        elif i * i > x:
            return i - 1


def mySqrtPlus(x: int) -> int:
    """
    二分查找思想
    :param x:
    :return:
    """
    l, r, ans = 0, x, -1
    while l <= r:
        mid = (l + r) // 2
        if mid * mid <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans


if __name__ == '__main__':
    x = 2
    res = mySqrt(x)
    print(res)
