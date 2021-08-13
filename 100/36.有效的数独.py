def is_valid_sudoku(board: list) -> bool:
    """
    根据输入的 9*9 数组 判断输入是的数字是否符合数独的规则，
    :param board: init array1
    :return: bool
    """
    rows = [{} for i in range(9)]
    columns = [{} for i in range(9)]
    block = [{} for i in range(9)]

    for i in range(9):
        for j in range(9):
            cur_num = board[i][j]
            if cur_num != '.':
                cur_num = int(cur_num)
                # 获取当前数组在块内的 index
                box_index = (i // 3) * 3 + j // 3

                # get(first_param,second_param),first_param 需要查询的字段, second_param 查询不到默认返回的信息
                rows[i][cur_num] = rows[i].get(cur_num, 0) + 1
                columns[i][cur_num] = rows[j].get(cur_num, 0) + 1
                block[i][cur_num] = rows[box_index].get(cur_num, 0) + 1

                # 只要出现的次数 大于 1 即说明不符合数独的规则
                if rows[i][cur_num] > 1 or columns[j][cur_num] > 1 or block[box_index][cur_num] > 1:
                    return False

    return True


if __name__ == '__main__':
    board = [
        ["8", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"]
    ]

    print(is_valid_sudoku(board))
