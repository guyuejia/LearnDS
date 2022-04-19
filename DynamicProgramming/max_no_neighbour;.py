# -*- coding: utf-8 -*-
'''
@File    :   max_no_neighbour;.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/19 9:28   gujiayue      1.0         None
'''
"""
从一个整数数组中获取一些不相邻的数，求这些不相邻的数之和的最大值
"""

"""
一、递归尝试
1，定义函数和参数，将游戏转换为一个普遍、局部的问题————从一个整数数组的子数组中获取不相邻的数据，求解数的和的最大值。
游戏道具本身是线性，且是游戏道具一直减少，是游戏结束的条件。所以设定数组左右边界是参数，可变参数猜测有2个，但根据后续的过程，实际只有1个right是可变的
2，定义主函数调用参数。0到有边界
3，basecase：当游戏道具（数组）只有1个元素时结束，right==left
4，确定等价转换关系，分析从递归过程中某个普通步骤下是如何转换到达最终步骤的————当某个状态[left,right]时，此时玩家有2个选择：
 先拿left位置的元素，然后递归[left+2,right]的部分；或者选择拿left+1的元素，然后递归[left+3,right]的部分。最终求最大值
二、是否有重复值
从递归过程中看明显有重复步骤
三、动态规划
1，根据递归函数，只有1个可变参数，所以一维缓存表即可,生成全0数组
2，纸上画一个一维表格，left变化范围是0到右边界。
3，根据递归basecase，生成表格中最右侧的值
4，分析普遍位置下，表格所依赖的值是当前表格右侧2位置和3位置的值，所以表格需要从右往左写
"""

def solve_by_recursive(arr):
    left = 0
    right = len(arr) - 1
    return recursive(arr,left,right)

def recursive(arr,left,right):
    if left > right:
        return 0

    if left == right:
        return arr[left]

    case1 = arr[left] + recursive(arr,left+2,right)
    case2 = arr[left + 1] + recursive(arr,left+3,right)

    return max(case1,case2)
def solve_by_dp(arr):
    right = len(arr) - 1
    dp_table = []
    for i in range(len(arr)):
        dp_table.append(0)
    #basecase，生成最右侧值
    dp_table[-1] = arr[-1]

    #普遍位置下的表格,从右往左,要处理越界的情况
    for i in range(right -1,-1,-1):
        dp_table[i] = max(arr[i] + pick(dp_table,i+2),arr[i+1] + pick(dp_table,i+3))
    # print(dp_table)
    return dp_table[0]
#index越界的情况下返回0，否则就返回该索引下的值
def pick(arr,index):
    if index > len(arr) -1:
        return 0
    else:
        return arr[index]


if __name__ == '__main__':
    arr = [2,10,2,1]
    print(solve_by_recursive(arr))
    print(solve_by_dp(arr))