def longestPalindrome(s):
    n = len(s)
    # 哨兵
    matrix = [[False] * n for i in range(n)]
    ans = ""
    """ l 只用于循环的次数，以及和 ans 长度进行比较.  """
    for l in range(n):
        for i in range(n):
            j = i + 1
            # 结束循环
            if j >= len(ans):
                break
            # 第一次进来，默认为 True
            if l == 0:
                matrix[i][j] = True
            # 第二次进来，需要进行比较
            elif l == 1:
                matrix[i][j] = (s[i] == s[j])
            # 其他情况
            else:
                # 用 i+1:j-1 && i == j 判断是否为回文串
                matrix[i][j] = (matrix[i + 1][j - 1] and s[i] == s[j])
            # 长度大于 ans 更新子串
            if matrix[i][j] and l + 1 > len(ans):
                ans = matrix[i:j + 1]
    return ans


if __name__ == '__main__':
    s = 'babad'
    res = longestPalindrome(s)
    # print('res', res)
