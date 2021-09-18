"""
    冒泡排序：
        每次外层循环结束之后，会将最大的一个值放在数组尾部
        双层for循环，
            第一层循环：代表循环的次数，
            第二层循环：代表每次循环交换的次数,当前位置和下一个值的进行比较
    时间复杂度：O(N*N)，最好情况O(n) 原本就是有序的序列
    空间复杂度：O(1)
    算法具有稳定性
"""


def bubble_sort(arr: list) -> list:
    l = len(arr)
    """外层循环，数组长度，需要循环的次数."""
    for i in range(l):
        """每次循环次数下，需要比较的次数，i -> l-i-1."""
        for j in range(l - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr


def cocktail_sort(arr: list) -> list:
    """
    升级版本的冒泡排序，但是效率依旧是O(N*N)
    :param arr:
    :return:
    """
    l, r = 0, len(arr) - 1
    while l < r:

        for i in range(l, r):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
        r -= 1

        for i in range(r, l, -1):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
        l += 1

    return arr


if __name__ == '__main__':
    arr = [1, 5, 6, 8, 2, 4, 9, 0, -1, 2]
    print(bubble_sort(arr))
    print(cocktail_sort(arr))
