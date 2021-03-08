def isPalindrome(x):
    x = str(x)
    l = len(x)
    flag = True
    for i, k in enumerate(x):
        if k != x[l - i - 1]:
            flag = False
            return False
    if flag:
        return True


if __name__ == '__main__':
    x = 121
    print(isPalindrome(x))
