def countAndSay(n: int) -> str:
    if n == 1:
        return "1"
    else:
        _res = "1"
        for i in range(1, n):

            _ls = list(_res)  # 转换为ls
            j = 0
            __res = ""  # 文本拼接
            _ls_len = len(_ls)
            while j < _ls_len:
                content = _ls[j]
                count = 1
                for m in range(j + 1, _ls_len):
                    if _ls[m] == content:  # 判断是否和下一个元素一致
                        count += 1
                    else:
                        break
                j += count
                __res += str(count) + str(content)
            _res = __res

        return _res


if __name__ == '__main__':
    res = countAndSay(5)
    print(res)
