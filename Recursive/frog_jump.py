# -*- coding: utf-8 -*-
'''
@File    :   frog_jump.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/1/11 17:18   gujiayue      1.0         None
'''
"""
小青蛙跳台阶
1，小青蛙一次可以跳1个台阶，或者2个台阶。求该青蛙跳上一个n级的台阶有多少种跳法
2，显然n越小，越简单计算，这种就可以考虑用递归的思想，不断把大问题分解为小问题
3，关键就是找到f(n)和f(n-1)之间的关系
3.1 跳n台阶，可以简化为先跳n-1个，然后再跳1个；或者先跳n-2个，再跳2个
3.2 f(n) = f(n-2) + f(n - 1)
"""

from timeit import timeit

#1,定义函数，确定参数
def jump(n):
    #2，结束条件
    if n <= 2:
        return n
    else:
        #3，等价式，并且参数不断缩小逼近结束条件
        return jump(n-1) + jump(n-2)
#动态规划版本
def jump2(n):
    steps = []
    #steps[0] = 0
    steps.append(0)
    #steps[1] = 1
    steps.append(1)
    #steps[2] = 2
    steps.append(2)
    for i in range(3,n+1):
        steps.append(steps[i-1]+steps[i-2])
    return steps[n]
n = 10

t1 = timeit("jump(30)","from __main__ import jump",number=50)
t2 = timeit("jump2(30)","from __main__ import jump2",number=50)
print(t1/t2)

