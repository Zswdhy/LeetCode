"""
    桶排序:
        计数排序的改进版本
        先进行分组----->不未空的桶进行内部排序----->按照桶的顺序进行元素追加.
        时间复杂度：O(n+k)
        空间复杂度：O(n+k)
        【注】：空间换时间的排序算法
"""
import random
from typing import List


def bucket_sort(arr: List[int]):
    """桶排序"""
    min_num = min(arr)
    max_num = max(arr)

    """和计数排序相比，减少桶的数量."""
    bucket_range = (max_num - min_num) / len(arr)
    """初始化桶."""
    count_list = [[] for i in range(len(arr) + 1)]
    """根据计算的桶数，桶元素追加."""
    for i in arr:
        count_list[int((i - min_num) // bucket_range)].append(i)

    arr.clear()
    """输出排序完毕的数组【每个桶内部调用sorted func】."""
    for i in count_list:
        for j in sorted(i):
            arr.append(j)


if __name__ == '__main__':
    arr = [random.randint(0, 100) for _ in range(10)]
    print("原始数据：", arr)
    bucket_sort(arr)
    print("桶排序结果：", arr)
