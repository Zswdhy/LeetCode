def search_insert(nums: list, target: int) -> int:
    """
    查找有序列表的左边界索引
    :param nums:
    :param target:
    :return:
    """
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if target == nums[mid]:
            return mid
        elif target < nums[mid]:
            r = mid - 1
        elif target > nums[mid]:
            l = mid + 1
    return l


if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target = 5
    res = search_insert(nums, target)
    print(res)
