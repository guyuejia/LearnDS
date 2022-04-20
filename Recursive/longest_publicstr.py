# -*- coding: utf-8 -*-
'''
@File    :   longest_publicstr.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/20 10:45   gujiayue      1.0         None
'''
"""
求解两个字符串的最长公共子串
"""

import timeit,functools
#暴力递归实现
def recursive(s1,s2):
    if s1 in s2:
        return s1
    case1 = recursive(s1[1:],s2)
    case2 = recursive(s1[:-1],s2)
    return case1 if len(case1)>len(case2) else case2

def f(A,B):
    list1=[]
    for i in range(len(A),0,-1):
        for j in range(0,len(A)-i+1):
            if A[j:j+i] in B:
                list1.append(A[j:j+i])
                return A[j:j+i]
        if list1:
            break

#直接迭代循环尝试，复杂度O(n2)
#以其中一个字符串为基础进行迭代，如果这个字符在另外一个字符串里，就追加下一个字符继续判断，直到不在另外一个字符串。
def direct_try(s1,s2):
    result = ""
    for i in range(0,len(s1)):
        tmp = s1[i]
        #判断当前子字符串是否在s2中
        while tmp in s2:
            # 更新结果
            result = tmp if len(tmp) > len(result) else result
            if i+1 >= len(s1):
                break
            #继续追加下一个字符进来
            tmp = tmp + s1[i+1]
            i = i + 1
    return result

if __name__ == '__main__':
    s1 = "cdfedeasasdfgasgag"
    s2 = "pmsedsfwengaeh"
    t1 = timeit.timeit(stmt="recursive(s1,s2)",setup="from __main__ import recursive",globals=globals(),number=100)
    # t1 = timeit.timeit(functools.partial(recursive,s1,s2),number=1000)
    print(recursive(s1,s2))
    print(f(s1,s2))
    t2 = timeit.timeit(stmt="f(s1,s2)", setup="from __main__ import recursive", globals=globals(), number=100)
    t3 = timeit.timeit(stmt="direct_try(s1, s2)", setup="from __main__ import recursive", globals=globals(), number=100)
    print(t1,t2,t3)