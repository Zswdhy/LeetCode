def longestPalindrome(s):
    n = len(s)
    # 哨兵
    matrix = [[False] * n for i in range(n)]
    ans = ""
    for l in range(n):

        for i in range(n):
            j = i + 1
            if j >= len(ans):
                break
            if l == 0:
                matrix[i][j] = True
            elif l == 1:
                matrix[i][j] = (s[i] == s[j])
            else:
                matrix[i][j] = (matrix[i + 1][j - 1] and s[i] == s[j])
            # 更新子串
            if matrix[i][j] and l + 1 > len(ans):
                ans = matrix[i:j + 1]
    return ans


if __name__ == '__main__':
    s = 'babad'
    res = longestPalindrome(s)
    # print('res', res)
