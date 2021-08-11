def search_insert(nums: list, target: int) -> int:
    """
    查找有序列表的左边界索引
    :param nums:
    :param target:
    :return:
    """
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            right = mid - 1
        elif target > nums[mid]:
            left = mid + 1
    return left


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    res = search_insert(nums, target)
    print(res)
