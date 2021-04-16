"""
111 --> AAA、KA
"""


def demo(new_s, i):
    if i == len(new_s):
        return 1
    if new_s[i] == '0':
        return 0

    if new_s[i] == '1':
        res = demo(new_s, i + 1)
        if i + 1 < len(new_s):
            res += demo(new_s, i + 2)
        return res
    elif new_s[i] == '2':
        res = demo(new_s, i + 1)
        if i + 1 < len(new_s) and new_s[i + 1] >= '0' and new_s[i + 1] <= '6':
            res += demo(new_s, i + 2)
        return res
    # new_s[i] '3' - '9'
    return demo(new_s, i + 1)


if __name__ == '__main__':
    print(demo('11111', 0))
