# -*- coding: utf-8 -*-
'''
@File    :   Knapsack.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/20 8:57   gujiayue      1.0         None
'''
"""
背包问题
给定两个长度都为N的数组weights和values，weights[i]和values[i]分别代表 i号物品的重量和价值，重量都是正数
给定一个正数bag，表示一个载重bag的袋子，装的物品不能超过这个重量
返回能装下的最大价值
"""

"""
一、递归尝试
1，定义函数和参数，将问题转为一个普遍的问题
    a.游戏主体是1个人
    b.游戏道具是线性的，且会逐渐减少，将数组的左右边界设置为参数，最终经后面的尝试，右边界其实是固定不变的参数。
    c.结束条件是其他也就是袋子的最大承重，将剩余承重设置为参数
    
2，主函数调用参数——0到右边界，背包最大容量
3，basecase——当背包剩余承重小于等于0时，游戏结束
4，递归等价转换，将游戏等价为递归过程中某个中间步骤转为最终结果————每当面临一堆物品时，有2个选择要么选择拿最左边的物品，要么不选择最左边物品，两种选择取最大值
二、是否有重复

三、动态规划
1，根据递归过程，可变参数是左边界和背包剩余重量，所以是二维缓存表
2，纸上画表格分析，行为物品索引，变化范围是0到len-1,列是背包重量，变化范围是0-bag，生成全0表
3, 分析basecase，rest为0的时候，也就是第0列都是0，left大于物品长度的时候，都是0，此时属于越界后
4，分析普遍情况的某个表格的依赖情况。由于要获取的最终值是表格的右上角，另外看递归过程，每个单元格依赖于下方和左侧的。所以需要从下往上，从左往右。
"""

def solve_by_recuisive(weights,values,bagsize):
    left = 0
    right = len(weights) - 1
    return recursive(weights,values,left,right,bagsize)

def recursive(weights,values,left,right,rest):
    """

    :param weights: 物品的重量
    :param values: 价值
    :param left:
    :param right:
    :param rest: 背包剩余的承重
    :return:
    """
    if left > right:
        return 0
    #basecase
    if rest <= 0:
        return 0

    # 不选择拿最左边物品
    case2 = recursive(weights, values, left + 1, right, rest)
    #选择拿最左边的物品,先判断该物品是否可以装的下
    if rest-weights[left] >= 0:
        case1 = values[left] + recursive(weights,values,left+1,right,rest-weights[left])
        #取最大值
        return max(case1,case2)
    else:
        return case2

def solve_dp(weights,values,bag):
    length = len(weights)
    dp_table = []
    for i in range(length):
        dp_table.append([])
        for j in range(bag+1):
            dp_table[i].append(0)

    #basecase,由于初始化的时候就都是0了，所以不用专门的写basecase了

    #写表,从下往上写,从左到右
    for i in range(length-1,-1,-1):
        for j in range(0,bag+1):
            case2 = pick(dp_table,i+1,j)
            if j - weights[i] >=0:
                case1 = values[i] + pick(dp_table,i+1,j-weights[i])
                dp_table[i][j] = max(case1,case2)
            else:
                dp_table[i][j] = case2
    return dp_table[0][bag]

def pick(dp,i,j):
    length = len(dp)
    if i >=length:
        return 0
    else:
        return dp[i][j]

if __name__ == '__main__':
    weights = [3, 2, 4, 7, 3, 1, 7]
    values = [5, 6, 3, 19, 12, 4, 2]
    weights = [5]
    values = [5]
    bag = 15
    print(solve_by_recuisive(weights,values,bag))
    print(solve_dp(weights,values,bag))