# -*- coding: utf-8 -*-
'''
@File    :   binarysearch.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/11 1:43   gujiayue      1.0         None
'''
"""
二分法查找有序数组里某个值的索引
复杂度O(logn)
思想很简单
但是具体代码编写有一点点难度：需要明确每次折半后的新数组的左右边界和中间值索引
"""

import time
def binary_search(l:list,target):
    """

    :param l: 有序数组
    :param target: 待查找的目标值
    :return: 返回目标值的索引
    """
    left = 0
    right = len(l)
    while True:
        tmp = l[left:right]
        #偶数长度，中间索引取右半边第一个
        #这样奇偶长度的中间值的索引都可用如下表达式表达
        #注意mid索引，要加上一个当前左边界的长度
        mid = len(tmp) // 2 + left
        # time.sleep(0.5)
        if target == l[mid]:
            return mid
        #无论奇偶长度，左右边界的更新都是如下规则，可以分别找个数组试试
        if target > l[mid]:
            left = mid + 1
        else:
            right = mid


if __name__ == '__main__':
    l = [-1,2,5,7,15,22,38,99,100]
    target = 15
    print(binary_search(l,target))