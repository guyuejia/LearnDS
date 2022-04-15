# -*- coding: utf-8 -*-
'''
@File    :   horse_jump.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/15 12:46   gujiayue      1.0         None
'''
"""
10行9列的棋盘 ，左下角坐标是（0，0），计算棋子“马”，从（0，0）位置出发，走K步，跳到（x,y)位置的方法数量
"""


def horse_jump(m, n, step):
    return jump_by_recursive(0, 0, m, n, step)


# 递归方法实现
def jump_by_recursive(x, y, m, n, step):
    """

    :param x: 起始坐标
    :param y:
    :param m: 目的坐标
    :param n:
    :param step: 步数
    :return:
    """

    # 基准条件。剩0步的时候，如果xy和mn相同就说明这是1种可行的方法
    if step == 0:
        if x == m and y == n:
            return 1
        else:
            return 0
    # 如果坐标越界，说明此路不通，返回0
    if x < 0 or x > 9 or y < 0 or y > 8:
        return 0
    # 下一步，棋子有8种跳法
    case1 = jump_by_recursive(x + 2, y + 1, m, n, step - 1)
    case2 = jump_by_recursive(x + 1, y + 2, m, n, step - 1)
    case3 = jump_by_recursive(x - 1, y + 2, m, n, step - 1)
    case4 = jump_by_recursive(x - 2, y + 1, m, n, step - 1)
    case5 = jump_by_recursive(x - 2, y - 1, m, n, step - 1)
    case6 = jump_by_recursive(x - 1, y - 2, m, n, step - 1)
    case7 = jump_by_recursive(x + 1, y - 2, m, n, step - 1)
    case8 = jump_by_recursive(x + 2, y - 1, m, n, step - 1)
    return case1 + case2 + case3 + case4 + case5 + case6 + case7 + case8

def jump_by_dp(m, n, step):
    # 初始化3维dp表
    dp_table = []
    for level in range(step + 1):
        dp_table.append([])
        for line in range(10):
            dp_table[level].append([])
            for column in range(9):
                dp_table[level][line].append(0)

    # 初始化basecase,step为0的情况
    dp_table[0][m][n] = 1
    # 构造其他层（step)的数值
    for level in range(1, step + 1):
        for line in range(10):
            for column in range(9):
                # print(level,line,column)
                case1 = pick(dp_table,line + 2, column + 1,  level - 1)
                case2 = pick(dp_table,line + 1, column + 2, level - 1)
                case3 = pick(dp_table,line - 1, column + 2,  level - 1)
                case4 = pick(dp_table,line - 2, column + 1,  level - 1)
                case5 = pick(dp_table,line - 2, column - 1,level - 1)
                case6 = pick(dp_table,line - 1, column - 2,  level - 1)
                case7 = pick(dp_table,line + 1, column - 2,  level - 1)
                case8 = pick(dp_table,line + 2, column - 1,  level - 1)
                dp_table[level][line][column] = case1 + case2 + case3 + case4 + case5 + case6 + case7 + case8
    # print(dp_table)

    return dp_table[step][m][n]

def pick(dp_table,x,y,level):
    if x < 0 or x > 9 or y < 0 or y > 8:
        return 0
    else:
        return dp_table[level][x][y]
if __name__ == '__main__':
    print(jump_by_dp(7, 7, 0))
    print(horse_jump(7, 7, 0))
