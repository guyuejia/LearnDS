# -*- coding: utf-8 -*-
'''
@File    :   longestPalindrome.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/7 11:21   gujiayue      1.0         None
'''
import timeit
#最暴力直接的递归实现
def longestPalindrome(s: str) -> str:
    if s == s[::-1]:
        return s
    s1 = longestPalindrome(s[1:])
    s2 = longestPalindrome(s[:-1])
    return s1 if len(s1) > len(s2) else s2

#返回最长的字串长度
def longestPalindrome1(s,L,R):
    # print(s[L:R+1])
    #边界条件
    if L == R:
        return 1
    if L == R-1:
        if s[L] == s[R]:
            return 2
        else:
            return 1
    length = longestPalindrome1(s, L + 1, R - 1)
    if s[L] == s[R]:
        # print("length:{}".format(length))
        case3 = 2 + length if length == R-L-1 else 1
        # print("case3:{}".format(case3))
    else:
        case3 = length
    # case3 = length if s[L] == s[R] and length == R-L-1
    case1 = longestPalindrome1(s,L+1,R)
    case2 = longestPalindrome1(s,L,R - 1)

    return max([case1,case2,case3])

s="aecaceaaaaaasdfe"
L = 0
R = len(s) - 1
t1 = timeit.timeit('longestPalindrome(s)',"from __main__ import longestPalindrome",number=10,globals={'s':s})
print(t1)
t2 = timeit.timeit('longestPalindrome1(s,L,R)',"from __main__ import longestPalindrome1",number=10,globals={'s':s,"L":L,"R":R})
print(longestPalindrome(s))
print(longestPalindrome1(s,L,R))
print(t1,t2)
