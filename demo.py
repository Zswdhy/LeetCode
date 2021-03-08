def child_sequence(s, index, ans, path):
    if index == len(s):
        if path not in ans:
            ans.append(path)
    else:
        choice_1 = path
        child_sequence(s, index + 1, ans, choice_1)
        choice_2 = path + s[index]
        child_sequence(s, index + 1, ans, choice_2)
    return ans


if __name__ == '__main__':
    s = 'aaaaaa'
    s = list(s)
    ans = []
    path = ""

    res = child_sequence(s, 0, ans, path)
    print(res)
