"""

给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 的那 两个 整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。

你可以按任意顺序返回答案。

"""


def demo(nums, target):
    # 暴力解法
    # for i in range(len(nums)):
    #     temp = target - nums[i]
    #     if temp in nums[i + 1:]:
    #         second = nums[i + 1:].index(temp)
    #         return i, second + i + 1

    # 模拟哈希映射
    hashmap = {}
    for ind, num in enumerate(nums):
        hashmap[num] = ind
    for i, num in enumerate(nums):
        j = hashmap.get(target - num)
        if j is not None and i != j:
            return [i, j]


if __name__ == '__main__':
    # nums = [3, 3]
    nums = [2, 7, 11, 15]
    target = 9
    demo(nums, target)
