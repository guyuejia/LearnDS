# -*- coding: utf-8 -*-
'''
@File    :   shortest_palindrome.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/18 12:15   gujiayue      1.0         None
'''
"""
最短的回文子串。
回文字符串特性：去掉两头的回文字符串，剩下的字符串还是回文字符串。
所以一个回文子串的最短长度，不算1的话，只能是2或者3。因为如果大于这个值的话，去掉两头的字符，也就是减2的话，剩下的字符串仍旧是回文。
因此可以通过求解字符串的最长子回文字符串长度，如果是奇数，那最短值就是3，如果是偶数那最短值就是2。
"""
import longest_palindromic

def solve(s):
    length = longest_palindromic.solve_by_dp(s)
    if length==1:
        return -1
    elif length % 2 == 0:
        return 2
    else:
        return 3

if __name__ == '__main__':
    s="ae"
    n = len(s)
    print(solve(s))