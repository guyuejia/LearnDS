# -*- coding: utf-8 -*-
'''
@File    :   stop_process.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/2/6 14:23   gujiayue      1.0         None
'''
"""
需求描述
某系统中有n个进程，每个进程都偶自己唯一的进程id(pid)，同时每个进程最多还有一个父进程，父进程id为（ppid）,和一个或者多个子进程。若某进程没有父进程，则ppid为0，当某一进程被中止时，其子进程也将被终止。  
现在给出进程id列表和其对应的父进程id列表，当要终止某一进程时，计算最终会终止哪些进程，并将要终止的PID按照升序排列。  
- 输入描述：
    - 第一行输入两个整数n和k，分别代表当前系统中运行的进程数量和要终止的进程pid
    - 第二行输入n个正整数，表示进程列表PID
    - 第三行输入n个正整数，表示进程列表PID对应父进程的PPID列表
- 输出描述：输入所有会被终止的进程pid，按照pid升序排列，每个pid用空格分格。
- 实例：
    - 输入：4 5  
	1 3 10 5  
	3 0 5 3  
    - 输出 5 10
"""
"""
问题分析：要结束的进程除了进程本身和它的子进程外，还应该包括子进程的子进程，也就是进程的后代都要一并终止。
可以考虑利用递归实现，每次递归只找出进程的子进程。直到找出来的子进程都没有儿子了，就停止
"""
import copy

line1 = "5 5"
line2 = "1 2 3 8 9"
line3 = "3 0 5 3 8"
#进程数量
nums = int(line1.split(" ")[0])
#要停止的进程id
stop_pid = line1.split(" ")[1]
pids = line2.split(" ")
ppids = line3.split(" ")
#定义字典，存储每个pid的孩子，k是进程id，v是集合，对应的是子进程集合
pid_to_childs = {}
#每个pid的父亲，k是进程id，v是父进程id
pid_to_father = {}
for i in range(nums):
    if ppids[i] not in pid_to_childs.keys():
        pid_to_childs[ppids[i]] = set()
    pid_to_childs[ppids[i]].add(pids[i])
#利用zip函数直接生成
pid_to_father = dict(zip(pids,ppids))

#存储所有需要停止的进程id集合
result = set()

#步骤1，定义递归函数,参数是一个集合
def find_childrens(ids:set):
    global result,pid_to_childs,pid_to_father
    result |= ids

    #步骤2，确定递归结束条件，也就是所有的进程都没有儿子的时候就停止
    if(len(ids & pid_to_childs.keys()) == 0):
        return result
    #步骤3，收敛参数，也就是将ids不断的收敛
    else:

        #找到ids里每个id的子进程
        all_childreds = set()
        for i in ids:
            if i in pid_to_childs.keys():
                all_childreds |= pid_to_childs[i]
        #将查找到的所有子进程作为参数，递归调用
        find_childrens(all_childreds)

find_childrens({stop_pid})
print(result)