def findSubstring(s, words):
    if not s or not words:
        return []

    once_len = len(words[0])
    all_len = len(''.join(words))
    word_dict = {}
    res = []

    for item in words:
        word_dict[item] = word_dict.get(item, 0) + 1

    for start in range(len(s) - all_len + 1):
        mid_temp = word_dict.copy()
        j = start + once_len
        # 当前的 value 在 words 内，并且哈希列表中的 value >= 1
        while s[j - once_len:j] in mid_temp and mid_temp[s[j - once_len:j]] > 0:
            mid_temp[s[j - once_len:j]] -= 1  # value - 1
            j += once_len  # 长度增加
        if sum(mid_temp.values()) == 0:  # value 为 0 时，结束
            res.append(start)

    return res


if __name__ == '__main__':
    s = "barfoothefoobarman"
    words = ["foo", "bar"]

    # s = "wordgoodgoodgoodbestword"
    # words = ["word", "good", "best", "word"]
    res = findSubstring(s, words)
    print(res)
