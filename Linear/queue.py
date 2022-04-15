# -*- coding: utf-8 -*-
'''
@File    :   queue.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/1/11 15:59   gujiayue      1.0         None
'''
"""
利用list实现队列
将list的尾部定为队列的尾部，添加元素在列表的最后添加，复杂度是1
删除元素也就是删除列表的头部，复杂是n
"""

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.append(item)

    def dequeue(self):
        self.items.pop(0)

    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)