# -*- coding: utf-8 -*-
'''
@File    :   isPalindrome.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/7 11:40   gujiayue      1.0         None
'''
#利用递归判断一个字符串是否为回文字符串
def isPalindrome(s:str)->bool:
    #基准条件
    if len(s) <= 1:
        return True
    else:
        #等效条件
        if s[0] == s[-1]:
            return isPalindrome(s[1:-1])
        else:
            return False

s="aav"
print(isPalindrome(s))