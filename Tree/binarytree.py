# -*- coding: utf-8 -*-
'''
@File    :   binarytree.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/3/22 15:48   gujiayue      1.0         None
'''
from typing import Optional
from queue import Queue

class TreeNode:
    """
    树节点
    """
    def __init__(self, val=0, left = None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BinaryTree:
    def __init__(self, rootObj):
        """

        :param rootObj: 要插入的节点的值
        """
        self.key = rootObj
        self.left = None
        self.right = None

    #插入左子树newNode,如果左子树存在，就将要插入的节点变为新的做左子树
    def insertLeft(self,newNode):
        if self.left == None:
            self.left = BinaryTree(newNode)
        else:
            node = BinaryTree(newNode)
            node.left = self.left
            self.left = node

    # 插入左子树newNode
    def insertRight(self, newNode):
        if self.right == None:
            self.right = BinaryTree(newNode)
        else:
            node = BinaryTree(newNode)
            node.right = self.right
            self.right = node

    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left
    def setRootVal(self,obj):
        self.key = obj
    def getRootVal(self):
        return self.key
    #先序遍历
    def preOrder(self):
        result = [self.key]
        if self.left:
            result += self.left.preOrder()
        if self.right:
            result += self.right.preOrder()
        return result
    #中序遍历
    def inOrder(self)->list:
        result = []
        if self.left:
            result += self.left.inOrder()
        result.append(self.key)
        if self.right:
            result += self.right.inOrder()
        return result

    #后序遍历
    def postOrder(self):
        result = []
        if self.left:
            result += self.left.postOrder()
        if self.right:
            result += self.right.postOrder()
        result.append(self.key)
        return result

    #层序遍历,通过一个队列实现
    def levelOrder(self):
        result = []
        q = Queue()
        q.put(self)
        while not q.empty():
            node = q.get()
            # print(type(node))
            result.append(node.key)
            if node.left:
                q.put(node.left)
            if node.right:
                q.put(node.right)
        return result

    # 层序遍历,通过一个队列实现,相比上一个层序遍历，返回一个二维数组，内层数组list代表了每一层的所有元素
    def levelOrder2(self):
        result = []
        q = Queue()
        #进入队列不仅仅是节点本身，而是额外多一个信息，就是该节点的层级,第一层的层级为0
        ele = (self,0)
        q.put(ele)
        while not q.empty():
            ele = q.get()
            #分别提取出节点本身和节点所处的层级
            node = ele[0]
            level = ele[1]
            if len(result) < level + 1:
                result.append([])
            result[level].append(node.key)
            if node.left:
                #左子元素的level自然是根元素的level+1
                q.put((node.left,level + 1))
            if node.right:
                q.put((node.right,level + 1))
        return result
    #通过递归实现层序遍历
    def levelOrder2ByRecusive(self):
        result = []
        if self is None:
            return result
        #这个是真正的递归调用函数,通过层数参数传递
        def level(node, depth):
            if len(result) < depth:
                result.append([])
            result[depth-1].append(node.key)
            if node.left:
                level(node.left,depth + 1)
            if node.right:
                level(node.right,depth + 1)
        level(self,1)
        return result

if __name__ == '__main__':
    r = BinaryTree("a")
    #print(r.getRootVal())
    r.insertLeft("b")
    r.insertRight("c")
    r.left.insertLeft("e")

    #print(r.left.preOrder())
    print("先序遍历结果：{}".format(r.preOrder()) )
    print("中序遍历结果：{}".format(r.inOrder()) )
    print("后序遍历结果：{}".format(r.postOrder()) )
    print("层序遍历结果：{}".format(r.levelOrder()) )
    print("层序遍历，按照每层返回结果：{}".format(r.levelOrder2()) )
    print("层序遍历，递归实现按照每层返回结果：{}".format(r.levelOrder2ByRecusive()) )


