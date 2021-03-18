# 暴力解法
def strStr(haystack, needle):
    """
    返回短传在长串中的位置
    :param haystack: 长串
    :param needle:  短串
    :return: index
    """
    L, n = len(needle), len(haystack)

    for start in range(n - L + 1):
        if haystack[start] != needle[0]:
            continue
        if haystack[start: start + L] == needle:
            return start
    return -1


# KMP 算法 模式串匹配 【Next 数组】，过于复杂
# Sunday 算法

if __name__ == '__main__':
    haystack = "a"
    needle = "a"

    index = strStr(haystack, needle)
    print(index)
