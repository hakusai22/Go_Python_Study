from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from typing import List, Tuple, Optional, Dict, Set
from collections import defaultdict, Counter, deque, OrderedDict, namedtuple
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, reduce
from copy import deepcopy
from io import BytesIO, IOBase
import random
import sys
import os

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')
INFMAX = float('inf')
'''
gcd(), ord(), chr(), lower(), upper() 最大公约数/ASCII字符数值/数值ASCII字符/小写/大写
startswith(s), endswith(s), find(), index(), count(s)  字符串是否以s开始的/字符串是否以s结尾的/查找返回的是索引/获取索引
isalpha(), isdigit(), space(),join()  判断是否全为字符/判断是否全为数字/判断是否为空格/拼接
eval() 字符串转换成列表、元组或者字典/
uniform(x, y), pow(x, y)# 随机生成下一个实数，它在[x,y]范围内/ x**y 运算后的值。
字典推倒式 {key: len(key) for key in list}
列表推倒式 [i for i in range(100) if i % 3 == 0] 可切片,可索引,可重复
集合推倒式 {i ** 2 for i in (1, 2, 3)}  不可索引,不可切片,不可重复元素
gcd为最大公约数, lcm为最小公倍数。
'''

def I():
    return input()

def II():
    return int(input())

def FI():
    return float(input())

def MII():
    return map(int, input().split())

def MFI():
    return map(float, input().split())

def LI():
    return list(input().split())

def LMII():
    return list(map(int, input().split()))

def LMFI():
    return list(map(float, input().split()))

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# -*- coding: utf-8 -*-
# @Author  : wheat
# @Time    : 2022/12/31 19:57

"""
数据范围
    1≤n≤10000,
    1≤b≤a≤10^5
"""

if __name__ == '__main__':
    def ksm(a, b, p):
        res = 1
        while b:
            if b & 1:
                res = res * a % p
            b >>= 1
            a = a * a % p
        return res

    def predefine(n, p):
        # 分别用来存阶乘和阶乘的逆元
        fact, infact = [1] + [0] * n, [1] + [0] * n
        # 初始化我们所有的阶乘和阶乘的逆元
        for i in range(1, n):
            fact[i] = fact[i - 1] * i % p
            infact[i] = infact[i - 1] * ksm(i, p - 2, p) % p
        return fact, infact

    n = II()
    p = 10 ** 9 + 7
    fact, infact = predefine(10 ** 5 + 10, p)
    while n:
        a, b = MII()
        print(fact[a] * infact[b] % p * infact[a - b] % p)
        n -= 1
