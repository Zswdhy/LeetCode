"""
    不开辟新的空间
"""


def removeDuplicates(nums):
    res = []
    for item in nums:
        if item not in res:
            res.append(item)

    return len(res), res


def removeDuplicates2(nums):
    l = len(nums)
    cur_index = 0
    for i in range(l - 1):
        if nums[i] == nums[i + 1]:
            nums[cur_index], nums[i] = nums[i], nums[cur_index]
            cur_index += 1

    return l - cur_index, nums[cur_index:]


# 快慢指针
def removeDuplicates3(nums):
    if not nums:
        return 0
    fast, slow = 0, 0
    while fast < len(nums):
        if nums[fast] == nums[slow]:
            fast += 1
        else:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


if __name__ == '__main__':
    # num = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    num = [1, 1, 2]

    l, res = removeDuplicates(num)
    print(l, res)

    index, a = removeDuplicates2(num)
    print(index, a)

    a1 = removeDuplicates3(num)
    print(a1)
