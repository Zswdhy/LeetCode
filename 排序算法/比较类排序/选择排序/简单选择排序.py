"""
    简单排序算法：
        每次循环的时候，将最小的一个放在有序序列的尾部
        时间复杂度：O(N*N)
        空间复杂度：O(1)
        稳定性：不稳定
    冒泡排序：
        每次循环，将一个最大的值放在序列的尾部
"""


def selection_sort(ls):
    for i in range(len(ls)):
        """记录当前的索引值."""
        cur_index = i
        for j in range(i, len(ls)):
            if ls[j] < ls[cur_index]:
                """修改索引值."""
                cur_index = j
        """循环结束之后，修改序列的值."""
        ls[i], ls[cur_index] = ls[cur_index], ls[i]
    return ls


if __name__ == '__main__':
    ls = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    selection_sort(ls)
