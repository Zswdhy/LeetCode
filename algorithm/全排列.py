def AllRange(listx, start, end):
    if start == end:
        for i in listx:
            print(i, end='')
        print()
    for m in range(start, end + 1):
        # 每次移动下标，改变列表元素
        listx[m], listx[start] = listx[start], listx[m]
        AllRange(listx, start + 1, end)
        # 恢复为初试状态
        listx[m], listx[start] = listx[start], listx[m]


list1 = [1, 2, 3, 4]
AllRange(list1, 0, 3)
