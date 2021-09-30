"""
    简单插入排序：
        1、从第一个元素开始，假定已经是有序序列
        2、取后面的元素，依次和前面元素进行比较
        3、如果该元素大于新元素，则将该元素向后移动一个位置
        4、重复
    时间复杂度：O(N*N)
    空间复杂度：O(1)
    稳定性:稳定
"""


def insertion_sort(ls):
    """
        循环次数为： 1 - len(ls)
        默认当前的元素是有序序列
        当前元素和有序序列进行比较，找到合适位置插入即可
    """

    for i in range(1, len(ls)):
        """循环遍历的次数，只需要和当前索引之前的元素比较."""
        preIndex = i - 1
        current = ls[i]
        while preIndex >= 0 and ls[preIndex] > current:
            ls[preIndex + 1] = ls[preIndex]
            preIndex -= 1
        """循环结束，即找到需要插入新元素的位置."""
        ls[preIndex + 1] = current
    return ls


if __name__ == '__main__':
    ls = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    res = insertion_sort(ls)
    print(res)
