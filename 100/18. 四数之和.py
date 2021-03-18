def fourSum2(nums, target):
    quadruplets = list()
    if not nums or len(nums) < 4:
        return quadruplets

    nums.sort()
    length = len(nums)
    for i in range(length - 3):
        # 过滤重复
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        # 考虑 target 为负数的情况
        if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
            break
        # if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
        #     continue

        for j in range(i + 1, length - 2):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                break
            # if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
            #     continue

            left, right = j + 1, length - 1
            while left < right:
                total = nums[i] + nums[j] + nums[left] + nums[right]
                if total == target:
                    quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                    # 过滤重复
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    right -= 1
                if total < target:
                    left += 1
                else:
                    right -= 1

    return quadruplets


if __name__ == '__main__':
    nums = [1, -2, -5, -4, -3, 3, 3, 5]
    target = -11

    res2 = fourSum2(nums, target)
    print('最终返回的结果', res2)
