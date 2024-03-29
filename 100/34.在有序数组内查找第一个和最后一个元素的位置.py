"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：
你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def searchRange(nums: list, target: int) -> list:
    """
    二分查找法
    :param nums:输入数组
    :param target:目标值
    :return:list
    """
    left, right = 0, len(nums) - 1
    if not nums:
        return [-1, -1]
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            if nums[left] == target and nums[right] == target:
                return [left, right]
            if nums[left] != target:  # 没找到 左边右移一位
                left += 1
            if nums[right] != target:  # 没找到 右边左移一位
                right -= 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return [-1, -1]


if __name__ == '__main__':
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    res_ls = searchRange(nums, target)
    print(res_ls)
