"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。
"""


def demo_2(str):
    finally_res = set()
    l = len(str)
    # rk 右移指针，ans 最终返回结果
    rk, ans = -1, 0
    for i in range(l):
        if i != 0:
            # 移除之前存在的元素
            finally_res.remove(str[i - 1])
        # print('字符串长度', finally_res)
        while rk + 1 < l and str[rk + 1] not in finally_res:
            finally_res.add(str[rk + 1])
            rk += 1
        # 计算 set 集合的长度
        ans = max(ans, rk - i + 1)
    return ans


if __name__ == '__main__':
    s = "abcabcbb"
    print(demo_2(s))
