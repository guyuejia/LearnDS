# -*- coding: utf-8 -*-
'''
@File    :   longestPalindrome.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/7 11:21   gujiayue      1.0         None
'''

"""
求解最长的回文子串
"""

#最暴力直接的递归实现
def longestPalindrome(s: str) -> str:
    if s == s[::-1]:
        return s
    s1 = longestPalindrome(s[1:])
    s2 = longestPalindrome(s[:-1])
    return s1 if len(s1) > len(s2) else s2

if __name__ == '__main__':
    s="aecaceaaaaaasdfe"
    print(longestPalindrome(s))


