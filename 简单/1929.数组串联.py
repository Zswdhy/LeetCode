"""
给你一个长度为 n 的整数数组 nums 。请你构建一个长度为 2n 的答案数组 ans ，数组下标 从 0 开始计数 ，对于所有的 0 <= i < n 的 i ，满足下述所有要求：

ans[i] == nums[i]
ans[i + n] == nums[i]
具体而言，ans 由两个 nums 数组 串联 形成。

"""
def getConcatenation(nums: list) -> list:
    nums.extend(nums)
    return nums


if __name__ == '__main__':
    nums = [1, 2, 1]
    res = getConcatenation(nums)
    print(res)
