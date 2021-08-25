"""
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
"""


def maxSubArray(nums: list) -> int:
    """
    方程：f(i) = max( f(i-1) + nums[i], nums[ix] )
    :param nums:
    :return:
    """
    max_sum = nums[0]
    pre = 0
    for item in nums:
        pre = max(pre + item, item)
        max_sum = max(pre, max_sum)

    return max_sum


if __name__ == '__main__':
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    res = maxSubArray(nums)
    print(res)
