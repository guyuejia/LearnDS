# -*- coding: utf-8 -*-
'''
@File    :   anoi.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/2/17 16:52   gujiayue      1.0         None
'''
"""
汉诺塔数量
从圆柱A移动n个圆盘到圆柱C，本质上等同于如下（把大象关冰箱分三步：）：
1，先从A，移动n-1个圆盘到圆柱B
2，在从A把最后一个最大的圆盘，移动到圆柱C
3，最后把B的n-1个圆盘移动到圆柱C
"""
n = int(input("汉诺塔的数量："))
#步骤1，定义一个函数，参数是移动的数量,以及要从哪个源圆柱src，移动到哪个目的圆柱des
def move(n,src,des):
    #下面4行代码是获取除src和des代表的那个立柱
    pans = ["a","b","c"]
    pans.remove(src)
    pans.remove(des)
    other = "".join(pans)
    #步骤2：中止条件
    if n == 1:
        print("{}->{}".format(src,des))
    else:
        #步骤3，等价关系，收敛参数n
        move(n-1,src,other)
        print("{}->{}".format(src, des))
        move(n-1,other,des)
#move(n,"a","c")

