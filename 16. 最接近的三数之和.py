"""
给定一个包括 n 个整数的数组 nums 和 一个目标值 target。
找出 nums 中的三个整数，使得它们的和与 target 最接近。
返回这三个数的和。假定每组输入只存在唯一答案。
"""


#  运行超时
def threeSumClosest(nums, target):
    n = len(nums)

    res = {}
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                temp = nums[i] + nums[j] + nums[k]
                res[temp] = abs(temp - target)

    temp = sorted(res.items(), key=lambda x: x[1])

    return temp[0][0]


def threeSumClosest1(nums, target):
    n = len(nums)

    if not nums or n < 3:
        return None
    nums.sort()
    # 赋最大值
    res = float('inf')
    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l = i + 1
        r = n - 1
        while l < r:
            cur_sum = nums[i] + nums[l] + nums[r]
            if cur_sum == target:
                return target
            if abs(cur_sum - target) < abs(res - target):
                res = cur_sum
            if cur_sum - target < 0:
                l += 1
            else:
                r -= 1
    return res


if __name__ == '__main__':
    nums = [38, 60, -3, -12, 48, 100, 17]
    target = -20
    res = threeSumClosest(nums, target)
    print('1', res)
    res2 = threeSumClosest1(nums, target)
    print('2', res2)
