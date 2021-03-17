"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
"""


# 此方法在 leetcode 测试容易超时
def maxArea(height):
    l = len(height)
    maxarea = 0
    for i in range(l):
        for j in range(i, l):
            temp = (j - i) * min(height[i], height[j])
            if temp >= maxarea:
                maxarea = temp

    return maxarea


# 双向指针
def maxArea2(height):
    L, R = 0, len(height) - 1
    max_area = 0
    while L < R:
        min_height = min(height[L], height[R])
        max_area = max(min_height * (R - L), max_area)
        # 每次移动最短边
        if height[L] < height[R]:
            L += 1
        else:
            R -= 1

    return max_area


if __name__ == '__main__':
    height = [4, 3, 2, 1, 4]

    res = maxArea(height)

    res2 = maxArea2(height)
    print(res)
