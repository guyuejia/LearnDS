# -*- coding: utf-8 -*-
'''
@File    :   mergesort.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/10 17:40   gujiayue      1.0         None
'''
"""
递归实现归并排序:分——治——合
复杂度为O(nlogn)
"""
#递归第一步：确定函数和参数
def merge_sort(nums:list):
    #第二步：确定终止条件
    if len(nums) == 1:
        return nums
    #第三步：等效关系式——大象关到冰箱分三步
    #1，先排序左半边数组
    #2，再排序右半边数组
    #3，合并排序后的左边和右边
    mid = len(nums) // 2
    l_nums = merge_sort(nums[:mid])
    r_nums = merge_sort(nums[mid:])
    result = merge(l_nums,r_nums)
    return result

def merge(l:list,r:list):
    """
    合并两个有序数组为另一个有序数组
    复杂度为O(n)
    :param l:
    :param r:
    :return:
    """
    result = []
    while len(l) != 0 and len(r) != 0:
        if l[0] <= r[0]:
            result.append(l[0])
            l = l[1:]
        else:
            result.append(r[0])
            r = r[1:]
    if len(l) == 0:
        result += r
    else:
        result += l
    return result
if __name__ == '__main__':
    l = [10,5,-1,6,9,0,1,8]
    l1 = [-1,5,6,10]
    l2 = [0,1,8,9]
    print(merge_sort(l))