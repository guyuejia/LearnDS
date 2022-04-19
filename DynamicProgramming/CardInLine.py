# -*- coding: utf-8 -*-
'''
@File    :   CardInLine.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/18 16:09   gujiayue      1.0         None
'''
"""
给定一个整型数组arr，代表数值不同的纸牌排成一条线
玩家A和玩家B依次拿走每张纸牌
规定玩家A先拿，玩家B后拿
但是每个玩家每次只能拿走最左或最右的纸牌
玩家A和玩家B都绝顶聪明
请返回最后获胜者的分数
"""

"""
解析思路：
一、递归尝试
1，定义函数和参数：把问题转为一个普遍的问题————由于该问题的解决是两个主体或者说是两个人一起参与解决的，所以得写两个递归函数。
转为普遍问题，两个人从数组的子数组里面轮流拿牌，由于游戏结束条件是道具本身，而且游戏道具是一维线性的，所以设置两个变化参数：左边界和右边界
2,主函数调用方法：调用的完整范围的数组，返回两个主体的最大值
3，basecase:当左边界和有边界重合的时候，说明牌没有了，游戏结束。first玩家，只有1张牌的时候，这个牌就是最后结果
    second玩家，只有1张的时候，结果是0，因为轮不到自己拿牌。
4，等价转换关系：first玩家，每一步都有两个选择————拿最左边或者最右边，然后再作为second玩家从剩下的牌里面选择，两者相加。由于最终结果是最大值，所以返回不同选择的最大值
    second玩家，同样每一步都有两个选择————但是只能作为first玩家从减去左边牌或者减去右边牌里面选择。
二、是否有重复
有重复
三、动态规划
1,根据递归函数有2个可变参数，left和right，变化范围都是0- （数组的长度-1），初始化二维全0表，由于2个递归，需要初始化2个表
2，纸上画一个二维表格，确定行代表的意义、参数变化范围，列代表的意义、参数变化范围。表格中每个元素对应的结果意思是：从arr[left:right+1]范围内的牌，拿到的结果
3，根据base，可以直接确定两个表格中对角线的值
4，分析普遍情况下，每个单元格的值依赖于另一个表中同位置上侧和右侧的值。所以写表需要按照从对角线向左下角的顺序,也就是从上倒下，从右到左。
"""
import copy
def solve_by_recursive(arr):
    left = 0
    right = len(arr) -1
    first = recursive_first(arr,left,right)
    second = recursive_second(arr,left,right)
    print("first玩家结果：{}".format(first))
    print("second玩家结果：{}".format(second))
    return max(first,second)

#先拿牌的函数
def recursive_first(arr,left,right):
    #边界条件
    if left > right:
        return 0
    #basecase
    if left == right:
        return arr[left]
    # if left +1 == right:
    #     return max(arr[left],arr[right])

    case1 = arr[left] + recursive_second(arr,left+1,right)
    case2 = arr[right] + recursive_second(arr,left,right-1)
    return max(case1,case2)

#后拿牌
def recursive_second(arr,left,right):
    if left > right:
        return 0

    #basecase
    if left == right:
        return 0

    case1 = recursive_first(arr,left+1,right)
    case2 = recursive_first(arr,left,right-1)
    return min(case1,case2)

def solve_by_dp(arr):
    #first缓存表
    dp_table_first = []
    n = len(arr)
    for i in range(n):
        dp_table_first.append([])
        for j in range(n):
            dp_table_first[i].append(0)
    #second缓存表
    dp_table_second = copy.deepcopy(dp_table_first)

    #初始化base的值，也就是对角线的值
    for i in range(n):
        dp_table_first[i][i] = arr[i]
        #由于本来就是0，所以这行可以不用写
        dp_table_second[i][i] = 0

    #写表
    for i in range(1,n):
        for j in range(i-1,-1,-1):
            dp_table_first[i][j] = max(arr[j] + dp_table_second[i][j+1] , arr[i] + dp_table_second[i-1][j])
            dp_table_second[i][j] = min(dp_table_first[i-1][j] , dp_table_first[i][j+1])

    # print(dp_table_first)
    # print(dp_table_second)
    first = dp_table_first[n-1][0]
    second = dp_table_second[n-1][0]
    print("first玩家结果：{}".format(first))
    print("second玩家结果：{}".format(second))
    return max(first, second)

if __name__ == '__main__':
    arr = [3]
    print(solve_by_recursive(arr))
    print(solve_by_dp(arr))
    arr = [8,100,10]
    print(solve_by_recursive(arr))
    print(solve_by_dp(arr))
    arr = [1,2,8,5,9]
    print(solve_by_recursive(arr))
    print(solve_by_dp(arr))