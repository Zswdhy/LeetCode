def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ''
    temp = sorted(strs, key=lambda x: len(x))
    l = len(temp[0])
    res = ''

    for i in range(l):
        cur = temp[0][i]
        all_num = [item[i] for item in strs]

        if cur in all_num and len(set(all_num)) == 1:
            res += cur
        else:
            break

    return res


def longestCommonPrefix2(strs):
    if len(strs) == 0:
        return ''
    temp = sorted(strs, key=lambda x: len(x))
    l = len(temp[0])
    res = ''
    flag = True
    for i in range(l):
        cur = temp[0][i]
        for item in strs:
            if cur != item[i]:
                flag = False
                break
        if flag:
            res += cur

    return res


# 官方，只需要比较最长串和最短串即可
def longestCommonPrefix3(strs):
    if not strs:
        return ""
    str0 = min(strs)
    str1 = max(strs)
    for i in range(len(str0)):
        if str0[i] != str1[i]:
            return str0[:i]
    return str0


# hello  test

# test

if __name__ == '__main__':
    strs = ["cir", "car"]
    result = longestCommonPrefix(strs)
