"""
    归并排序：
        多个分组--->多次分组排序---->整体排序
        时间复杂度：O(nlog2n)
        空间复杂度：O(n)
        稳定性：稳定
"""


def merge(left, right):
    res = []
    l, r = 0, 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            res.append(left[l])
            l += 1
        else:
            res.append(right[r])
            r += 1
    if l == len(left):
        """此时说明，left数组的值全部使用完毕."""
        res.extend(right[r:])
    else:
        """此时说明，right数组的值全部使用完毕."""
        res.extend(left[l:])
    return res


def merge_sort(ls: list) -> list:
    if not ls:
        return []
    elif len(ls) == 1:
        return ls
    else:
        mid_index = len(ls) // 2
        left = merge_sort(ls[:mid_index])
        right = merge_sort(ls[mid_index:])
        return merge(left, right)


if __name__ == '__main__':
    ls = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    merge_sort(ls)
