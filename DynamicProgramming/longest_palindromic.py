# -*- coding: utf-8 -*-
'''
@File    :   longest_palindromic.py    
@Contact :   hushishuai.fly@hotmail.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2022/4/19 10:46   gujiayue      1.0         None
'''
"""
求解一个字符串的最长回文子串的长度
"""
"""
一、递归尝试
1，定义函数和参数，转换为一个普遍的问题
    a.游戏主体是1个，1个函数即可
    b.游戏道具是线性的，游戏过程中道具越来越少，所以考虑将左边界和右边界设置为参数
    c.游戏道具本身是结束的条件
2，主函数调用方法——0到右边界
3，basecase——left == right的时候，返回长度1
4，递归等效转换，分析递归过程中的某中间步骤如何转为求解最终的值————有四种尝试的可能，求解最大的值
二、是否重复
从递归过程中可看到有明显重复
三、动态规范
1,根据递归，有2个变化的参数，所以需要一个二维缓存表
2，纸上画一个表格，行代表了有边界right，范围是0到数组长度-1，列代表左边界，范围同样是0到数组长度-1。表中的每个单元格[left,right]，代表了字符串arr[left:right+1]的最长回文串长度
  最终游戏要求的结果是dp_table[0][right]的值
3，basecase，对角线上的值是1，对角线右上的部分都是0
4，分析普遍状态下的值的依赖。每个单元格都依赖其右侧，上侧和右上侧的值。写的过程根据对角线向左下，也就是是从上到下，从右到左
"""

from Recursive import isPalindrome

#递归解法
def solve_by_recursive(arr):
    right = len(arr) -1
    return recursive(arr,0,right)

def recursive(arr,left,right):
    #边界条件
    if left > right or right<0:
        return 0
    #basecase
    if left == right:
        return 1

    #有四种选择,
    # 1.arr[left,right-1]
    # 2.arr[left+1,right]
    # 3.arr[left+1,right-1] ,left和right索引的值不相等，求解中间的字符串
    # 4. 2 + arr[left+1,right-1]，left和right索引的值相等，并且中间字符是回文字符串
    length = recursive(arr, left + 1, right - 1)
    if arr[left] == arr[right]:
        #此处有两种做法
        #做法1，通过判断中间的字符串是否是回文串
        #做法2，同样递归调用，判断中间字符串的最长回文子串的长度是否为字符串的长度
        if isPalindrome.isPalindrome(arr[left+1:right]):
            case1 = 2 + length
        else:
            case1 = 0
    else:
        case1 = length
    case2 = recursive(arr,left+1,right)
    case3 = recursive(arr,left,right-1)
    #返回最大值
    return max(case1,case2,case3)

def solve_by_dp(arr):
    length = len(arr)
    dp_table = []
    #初始化为全0
    for row in range(length):
        dp_table.append([])
        for col in range(length):
            dp_table[row].append(0)
    #basecase
    for i in range(length):
        dp_table[i][i] = 1

    #写tp_table
    for row in range(1,length):
        for col in range(row-1,-1,-1):
            corner = dp_table[row-1][col+1]
            # print(row,col)
            if arr[row] == arr[col]:
                if isPalindrome.isPalindrome(arr[col+1:row]):
                    case1 = 2 + corner
                else:
                    case1 = 0
            else:
                case1 = corner
            case2 = dp_table[row][col+1]
            case3 = dp_table[row-1][col]
            dp_table[row][col] = max(case1,case2,case3)
    # print(length-1)
    # print(dp_table[length-1])
    return dp_table[length-1][0]



if __name__ == '__main__':
    str1 = "acasdfweasdeefsdt"
    print(solve_by_recursive(str1))
    print(solve_by_dp(str1))