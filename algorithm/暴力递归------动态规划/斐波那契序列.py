"""
    递归算法，会造成一些数值计算多次
"""

def func(n):
    if n == 1 or n == 2:
        return 1
    else:
        return func(n - 1) + func(n - 2)


def func2(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    elif n >= 3:
        ls = [1, 1]
        for i in range(2, n):
            ls.append(ls[i - 1] + ls[i - 2])

        return ls
    return False
