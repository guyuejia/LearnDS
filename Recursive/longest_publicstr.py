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
#暴力递归实现
def recursive(s1,s2):
    if s1 in s2:
        return s1
    case1 = recursive(s1[1:],s2)
    case2 = recursive(s1[:-1],s2)
    return case1 if len(case1)>len(case2) else case2

if __name__ == '__main__':
    s1 = "aocdfet"
    s2 = "pmcdfa"
    print(recursive(s1,s2))