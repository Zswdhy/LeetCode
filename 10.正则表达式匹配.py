def isMatch(s: str, p: str):
    import re
    if len(s) > 1 and len(p) == 1:
        return False
    res = re.search(p, s)

    if res:
        if res.group() == s:
            return True
        else:
            return False

    return False


if __name__ == '__main__':
    # s = "mississippi"
    # p = "mis*is*p*."

    s = "ab"
    p = ".*c"
    res = isMatch(s, p)
    print('返回结果', res)
