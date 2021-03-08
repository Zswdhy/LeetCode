def AllRange(listx, start, end):
    """
    :param listx: 元素列表
    :param start: 起始位置
    :param end: 终止位置
    :return:
    """
    if start == end:
        print('元素', listx)
        # for i in listx:
        #     print(i, end='')
        # print()
    flag_list = []
    for m in range(start, end):
        # 标记去重
        if listx[m] not in flag_list:
            flag_list.append(listx[m])
            # 每次移动下标，改变列表元素
            listx[m], listx[start] = listx[start], listx[m]
            AllRange(listx, start + 1, end)
            # 恢复为初试状态,恢复现场【主函数中的形式，方便下一次递归的初始形态一样】
            listx[m], listx[start] = listx[start], listx[m]


list1 = [1, 2, 3, 3, 5]
AllRange(list1, 0, 5)
