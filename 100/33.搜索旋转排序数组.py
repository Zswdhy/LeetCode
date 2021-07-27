"""
整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


def search(nums: list, target: int) -> int:
    """
    暴力解法
    :param nums: 输入数组
    :param target: 目标值
    :return: index
    """
    if target in nums:
        return nums.index(target)
    return -1


def search_plus(nums: list, target: int) -> int:
    """
    二分查找，因为 list 是部分有序，因此不能直接使用二分查找法
    平均的时间复杂度为：log(n)
    最坏的时间复杂度为：O(n)
    :param nums: 输入数组
    :param target: 目标值
    :return: index
    """
    left, right = 0, len(nums)
    while left <= right:
        mid_index = (left + right) // 2
        if nums[mid_index] == target:
            return mid_index
        elif nums[mid_index] > target:
            """ 
                当前中间值大于目标值，但是目标值在 [left,mid_index] 这样的区间，
                因此所可能存在的范围在 [left,mid_index_1] 区间内 
            """
            if nums[left] <= target < nums[mid_index]:
                right = mid_index - 1
            else:
                left = mid_index + 1
        else:
            """ 同理 """
            if nums[mid_index] < target <= nums[right]:
                left += 1
            else:
                right -= 1
    return -1


if __name__ == '__main__':
    # nums = [0, 1, 2, 4, 5, 6, 7]
    # target = 4
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0

    index = search_plus(nums, target)
    print('index pos', index)
