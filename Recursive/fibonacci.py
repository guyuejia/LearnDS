# -*- coding: utf-8 -*-
'''
@File    :   fibonacci.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/1/11 17:12   gujiayue      1.0         None
'''
from  timeit import timeit
"""
斐波那契数列的实现
"""
tmp_status = {}

def f(n):
    if n <= 2:
        return 1
    else:
        return f(n-1) + f(n-2)

#优化后的实现，保存中间计算的结果
def f_optimize(n):
    global tmp_status
    if n <= 2:
        return 1
    else:
        if n not in tmp_status.keys():
            tmp_status[n] = f(n-1) + f(n-2)
        return tmp_status[n]

t1 = timeit("f_optimize(30)","from __main__ import f_optimize",number=100)
print(t1)

t2 = timeit("f(30)","from __main__ import f",number=100)
print(t2)