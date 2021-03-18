def removeElement2(nums, val):
    fast = 0
    slow = 0

    while fast < len(nums):
        if nums[fast] != val:
            # 将不相等的元素移植到慢指针的位置
            nums[slow] = nums[fast]
            # 满指针加1
            slow += 1
        # 快指针元素 == val 快指针 ＋ 1
        fast += 1
    return slow


def removeElement3(nums, val):
    a = nums.count(val)
    for i in range(a):
        nums.remove(val)
    return len(nums)


if __name__ == '__main__':
    nums = [3, 2, 2, 3]
    val = 3
    print(removeElement2(nums, val))
    nums = [3, 2, 2, 3]
    val = 3
    print(removeElement3(nums, val))
