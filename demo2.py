import time


def func(n):
    dicts = {}
    if n == 1 or n == 2:
        return 1
    else:
        if f'{n - 1}' not in dicts.keys():
            dicts[f'{n - 1}'] = func(n - 1)
        if f'{n - 2}' not in dicts.keys():
            dicts[f'{n - 2}'] = func(n - 2)

        return func(n - 1) + func(n - 2)


if __name__ == '__main__':
    start = time.time()
    res = func(200)
    print(res)
    end = time.time()

    print(end - start)
