# -*- coding: utf-8 -*-
'''
@File    :   bubblesort.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/10 17:54   gujiayue      1.0         None
'''
"""
冒泡排序
复杂度O(n2)
"""
def bubble_sort(nums:list):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            #每次都与第一个值比较，确保循环一遍后，第一个值是最小的
            if nums[i] > nums[j]:
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
    return nums
if __name__ == '__main__':
    l = [10,5,-1,6,9,0,1,8]
    print(l)
    print(bubble_sort(l))