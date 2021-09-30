"""
    算法：
        选定一个初始值【第一个值】，
        每次循环的时候，两边进行，比初始值小的放在左边，比初始值大的放在右边
        递归调用
    时间复杂度：最好情况 O(nlog2n) 最坏 O(n*n)
    空间复杂度：
"""


def quick_sort(ls, start, end):
    """快速排序"""
    if start >= end:
        return
    mid = ls[start]
    low = start
    high = end
    while low < high:
        while low < high and ls[high] >= mid:
            high -= 1
        """修改左边位置上的元素."""
        ls[low] = ls[high]
        while low < high and ls[low] < mid:
            low += 1
        """修改右边位置上的元素."""
        ls[high] = ls[low]

    """将初始值赋值在空位置内."""
    ls[low] = mid
    """左边调用."""
    quick_sort(ls, start, low - 1)
    """右边调用."""
    quick_sort(ls, low + 1, end)


if __name__ == '__main__':
    ls = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    quick_sort(ls, 0, len(ls) - 1)
    print(ls)
