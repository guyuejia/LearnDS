# -*- coding: utf-8 -*-
'''
@File    :   reverse_list.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/1/11 17:58   gujiayue      1.0         None
'''
"""
递归反转单向列表
"""
class Node:
    def __init__(self,num,next = None):
        self.num = num
        self.next = next

class LinkList:
    def __init__(self,node = None):
        self.head = node
    def initByList(self,datalist):
        self.head = Node(datalist[0])
        p = self.head
        for i in datalist[1:]:
            tmp = Node(i)
            p.next = tmp
            p = p.next

    def printLink(self):
        if self.head == None:
            return
        t = self.head
        while t != None:
            print(t.num,end = " ")
            t = t.next
#1,定义函数，参数就是一个列表
def reverse(link:LinkList):
    #2，结束条件，当链表就1个元素时，直接返回本身
    if link.head.next == None:
        return link
    else:
        #3，确定等价关系。先翻转除第一个元素以外的链表，再把第一个元素接到翻转后的链表最后
        result = reverse(LinkList(link.head.next))
        # 把第一个元素的next，也就是第二个元素，也就是翻转后的链表的最后一个元素，把它的next 指向原链表的第一个元素
        link.head.next.next = link.head
        #再把第一个元素的next指向none
        link.head.next = None
        return result


if __name__ == '__main__':
    l = [1,2]
    link = LinkList()
    link.initByList(l)
    link.printLink()
    print()
    result = reverse(link)
    result.printLink()



