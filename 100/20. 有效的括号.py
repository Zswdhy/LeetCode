def isValid(s):
    details = {'(': ')', '{': '}', '[': ']'}
    ls = []
    for item in s:
        if item in details:
            ls.append(item)
        else:
            if len(ls) > 0 and details[ls[-1]] == item:
                ls.pop()
            else:
                return False
    if len(ls) == 0:
        return True
    return False


def isValid2(s):
    dic = {'{': '}', '[': ']', '(': ')', '?': '?'}
    stack = ['?']
    for c in s:
        if c in dic:
            stack.append(c)
        elif dic[stack.pop()] != c:  # 每次取最后一个元素与未入栈的元素进行比较
            return False
    return len(stack) == 1


s = "(])"

res = isValid(s)
print('res', res)
