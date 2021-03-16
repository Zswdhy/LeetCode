# 在 leetcode 测试超时
def threeSum(nums):
    if not nums or len(nums) < 3:
        return []
    l = len(nums)
    res = []
    for i in range(l):
        for j in range(i + 1, l):
            if -(nums[i] + nums[j]) in nums[j + 1:l]:
                temp = sorted([nums[i], nums[j], -(nums[i] + nums[j])])
                if temp not in res:
                    res.append(temp)
    return res


def threeSum2(nums):
    res = []
    nums = sorted(nums)
    if not nums or len(nums) < 3 or nums[0] > 0:
        return []

    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1
        # 当前状态的元素 > 0 直接结束
        if nums[i] > 0:
            return res

        while l < r:
            if nums[i] + nums[l] + nums[r] == 0:
                temp = sorted([nums[i], nums[l], nums[r]])
                if temp not in res:
                    res.append(temp)
                l += 1
                r -= 1
            elif nums[i] + nums[l] + nums[r] > 0:
                r -= 1
            elif nums[i] + nums[l] + nums[r] < 0:
                l += 1
    return res


def threeSum3(nums):
    n = len(nums)
    if (not nums or n < 3):
        return []
    nums.sort()
    res = []
    for i in range(n):
        if (nums[i] > 0):
            return res
        if (i > 0 and nums[i] == nums[i - 1]):
            continue
        L = i + 1
        R = n - 1
        while (L < R):
            if (nums[i] + nums[L] + nums[R] == 0):
                res.append([nums[i], nums[L], nums[R]])
                while (L < R and nums[L] == nums[L + 1]):
                    L = L + 1
                while (L < R and nums[R] == nums[R - 1]):
                    R = R - 1
                L = L + 1
                R = R - 1
            elif (nums[i] + nums[L] + nums[R] > 0):
                R = R - 1
            else:
                L = L + 1
    return res


import time

if __name__ == '__main__':
    nums = [-2, 0, 1, 1, 2]

    # res = threeSum(nums)

    start1 = time.time()
    print(len(threeSum2(nums)))
    end1 = time.time()
    print('1', end1 - start1)

    start2 = time.time()
    print(len(threeSum3(nums)))
    end2 = time.time()
    print('1', end2 - start2)
