# -*- coding: utf-8 -*-
'''
@File    :   RobotWalk.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/18 13:15   gujiayue      1.0         None
'''
"""
假设有排成一行的N个位置记为1~N，N一定大于或等于2
开始时机器人在其中的M位置上(M一定是1~N中的一个)
如果机器人来到1位置，那么下一步只能往右来到2位置；
如果机器人来到N位置，那么下一步只能往左来到N-1位置；
如果机器人来到中间位置，那么下一步可以往左走或者往右走；
规定机器人必须走K步，最终能来到P位置(P也是1~N中的一个)的方法有多少种
给定四个参数 N、M、K、P，返回方法数
"""

def solve_by_recursive(N,start,end,step):
    #主函数调用过程
    return recursive(start,end,step,N)


#递归方法
#定义一个普遍状态的递归函数：从任意位置出发走rest步数，到特定目标位置，的方法数
#递归规程中，不变的参数是；aim和N
#变化从参数是：cur和rest
def recursive(cur,aim,rest,N):
    """
    返回机器人从当前位置cur出发，走rest步数，最终到aim位置，的方法
    :param cur:
    :param aim:
    :param rest:
    :param N:
    :return:
    """
    if rest == 0:
        if cur == aim:
            return 1
        else:
            return 0

    #问题等效转换为：先从cur位置走到下个位置cur_next,然后从rest_next走rest-1步到aim位置的方法数，
    #当前位置cur在左边界,下一步只能右走
    if cur == 1:
        return recursive(2,aim,rest-1,N)
    #当前位置start在右边界，下一步只能左走
    if cur == N:
        return recursive(cur-1,aim,rest-1,N)
    #当前位置是中间位置，下一步左右都能走
    return recursive(cur-1,aim,rest-1,N) + recursive(cur+1,aim,rest-1,N)


def solve_by_dp(N,start,end,step):
    #有2个变化参数start和step，初始化一个二维表
    #该表的含义dp_table[i][j]代表了，从j位置出发，走i步到达end位置的方法数
    dp_table = []
    #row代表了剩余的步数，变化范围0-step
    for row in range(step+1):
        dp_table.append([])
        #col代表了当前位置，变化范围1-N,但是由于索引是从0开始，所以可以认为索引为0的这一列无用。
        for col in range(0,N+1):
            dp_table[row].append(0)

    #初始化basecase情况:第0行第end位置时为1，其余为0
    # print(dp_table)
    dp_table[0][end] = 1

    #分析依赖关系，表应该从上往下写
    #根据递归中的等价关系写表
    for rest in range(1,step +1):
        for cur in range(1,N+1):
            if cur == 1:
                dp_table[rest][cur]= dp_table[rest - 1][2]
            elif cur == N:
                dp_table[rest][cur] = dp_table[rest - 1][cur-1]
            else:
                dp_table[rest][cur] = dp_table[rest -1][cur-1] + dp_table[rest -1][cur+1]
    return dp_table[step][start]

if __name__ == '__main__':
    N = 7
    start = 2
    end = 4
    step = 6
    print(solve_by_recursive(N, start, end, step))
    print(solve_by_dp(N, start, end, step))