# -*- coding: utf-8 -*-
'''
@File    :   factorial.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/1/11 17:05   gujiayue      1.0         None
'''
"""
递归实现阶乘
"""

#第一要素，确定函数做什么和参数
def f(n):
    #第二要素，确定参数是什么时，直接结束递归，返回值
    if n <= 2:
        return n
    else:
        #第三要素,找到关系等价式，并且参数不断缩小逼近
        return n * f(n-1)

print(f(7))