def letterCombinations(digits):
    mapping = {"2": 'abc', "3": 'def', "4": 'ghi', "5": 'jkl', "6": 'mno', "7": 'pqrs', "8": 'tuv', "9": 'wxyz`'}
    if len(digits) == 0:
        return []

    def func(index):
        # 符合条件，注意 return ，清除 index 恢复现场
        if index == len(digits):
            result.append(','.join(cur_res))
            return

        letter = digits[index]
        for item in mapping[letter]:
            cur_res.append(item)
            func(index + 1)  # 层级
            cur_res.pop()  # 删除最后一个元素，返回上层递归

    result = []
    cur_res = []
    func(0)
    return result


def letterCombinations2(digits):
    KEY = {'2': ['a', 'b', 'c'],
           '3': ['d', 'e', 'f'],
           '4': ['g', 'h', 'i'],
           '5': ['j', 'k', 'l'],
           '6': ['m', 'n', 'o'],
           '7': ['p', 'q', 'r', 's'],
           '8': ['t', 'u', 'v'],
           '9': ['w', 'x', 'y', 'z']}
    if digits == '':
        return []
    ans = ['']
    for num in digits:
        ans = [pre + suf for pre in ans for suf in KEY[num]]
    return ans


if __name__ == '__main__':
    digits = '234'
    res = letterCombinations(digits)
    print(res)
