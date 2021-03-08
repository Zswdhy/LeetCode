"""
子串：必须连续，且位置不可以错误
"""

s = 'abcd'

l = len(s)
for i in range(l):
    temp = ''
    for j in range(i, l):
        temp += s[j]
        print(temp, end=" ")
    print()
