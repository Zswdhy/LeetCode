def intToRoman(num):
    hashmap = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L',
               40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}
    res = ''
    for key in hashmap:
        print('key', key)
        # 满足情况的 key
        if num // key != 0:
            count = num // key  # 比如输入4000，count 为 4
            print('count', count)
            res += hashmap[key] * count
            num %= key
            print('num', num)
        print('-' * 50)
    return res


if __name__ == '__main__':
    # 1 <= num <= 3999

    num = 1288

    res = intToRoman(num)
    print(res)
