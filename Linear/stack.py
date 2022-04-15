# -*- coding: utf-8 -*-
'''
@File    :   stack.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/1/11 15:06   gujiayue      1.0         None
'''

"""
利用list简单实现一个栈数据结构
限制只在list的最末端，作为栈的顶
"""

class Stack:
    def __init__(self):
        self.items = []

    def pop(self):
        self.items.pop()

    def push(self,x):
        self.items.append(x)

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(4)
    stack.isEmpty()
    stack.pop()
    stack.peek()


