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
# @Author  : zero
# @Time    : 2022/12/26 21:17

"""
基本思想：
    如果 N = a1 ^ k1 * a2 ^ k2 * ...an ^ kn
    约数个数： (k1 + 1) * (k2 + 1) * ...(kn + 1)
    约数之和： (a1 ^ 0 + a1 ^ 1 + ... + a1 ^ k1) * ... * (an ^ 0 + an ^ 1 + ... + an ^ kn)
    
    
    (a1 ^ 0 + a1 ^ 1 + ... + a1 ^ k1)
    其中的每一小项用秦九韶算法来计算：while (k1 -- ) t = (t * a1 + 1) % mod;
"""

mod = int(1e9 + 7)
primes = {}
a = II()
while a:
    a -= 1
    n = II()
    i = 2
    while i <= n // i:
        while n % i == 0:
            n //= i
            if i in primes:
                primes[i] += 1
            else:
                primes[i] = 1
        i += 1
    if n > 1:
        if n in primes:
            primes[n] += 1
        else:
            primes[n] = 1
res = 1
for i, val in primes.items():
    t = 1
    while val:
        val -= 1
        t = (t * i + 1) % mod
    res = res * t % mod
print(res)
