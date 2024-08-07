from bisect import bisect_left, bisect_right, insort_left, insort_right, insort, bisect
from math import ceil, floor, pow, gcd, sqrt, log10, fabs, fmod, factorial, inf, pi, e
from heapq import heapify, heapreplace, heappush, heappop, heappushpop, nlargest, nsmallest
from collections import defaultdict, Counter, deque
from itertools import permutations, combinations, combinations_with_replacement, accumulate, count, groupby, pairwise
from queue import PriorityQueue, Queue, LifoQueue
from functools import lru_cache, cache, reduce
from typing import List, Optional
import sys

from sortedcontainers import SortedList, SortedDict, SortedSet

sys.setrecursionlimit(10001000)

MOD = int(1e9 + 7)
INF = int(1e20)
INFMIN = float('-inf')  # 负无穷
INFMAX = float('inf')  # 正无穷
PI = 3.141592653589793
direc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
direc8 = [(1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
ALPS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
alps = 'abcdefghijklmnopqrstuvwxyz'

'''
gcd(), ord(), chr(), lower(), upper() 最大公约数/ASCII字符数值/数值ASCII字符/小写/大写
startswith(s), endswith(s), find(), index(), count(s)  字符串是否以s开始的/字符串是否以s结尾的/查找返回的是索引/获取索引
isalpha(), isdigit(), space(),join()  判断是否全为字符/判断是否全为数字/判断是否为空格/拼接
eval() 字符串转换成列表、元组或者字典/
uniform(x, y), pow(x, y)# 随机生成下一个实数，它在[x,y]范围内/ x**y 运算后的值。
字典推倒式 {key: len(key) for key in list}
列表推倒式 [i for i in range(100) if i % 3 == 0] 可切片,可索引,可重复
集合推倒式 {i ** 2 for i in (1, 2, 3)}  不可索引,不可切片,不可重复元素
'''



def rep():
    a = list(map(int, input().split()))
    return a

def sep():
    a = input().rstrip('\n')
    return a

# --idea 
# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2023/11/27 11:28
#
# 给定一个放有字母和数字的数组，找到最长的子数组，且包含的字母和数字的个数相同。
# 返回该子数组，若存在多个最长子数组，返回左端点下标值最小的子数组。若不存在这样的数组，返回一个空数组。

class Solution:
    def findLongestSubarray(self, array: List[str]) -> List[str]:
        # 初始化 前缀和0是符合条件 添加一个默认的点
        # key为前缀和 value是前缀和的下标
        vis = {0: -1}
        # s表示前缀和，mx表示最长子数组的长度，k表示最长子数组的左端点
        s = mx = k = 0
        for i, x in enumerate(array):
            s += 1 if x.isalpha() else -1
            # s 如果再set中已经出现过 说明两个点的前缀和相减等于0 两个点之间就是符合的长度
            # 第一次出现 sss 的位置为 j，那么区间 [j+1,..,i] 的子数组和就为 0
            # 第一次出现前缀和为3 下标j 第二次出现前缀和为3 下标i i-j 就是长度 中间有多少个数(1-0)=1
            if s in vis:
                j = vis[s]
                if mx < i - j:
                    mx = i - j
                    k = j + 1
            else:
                vis[s] = i
        return array[k: k + mx]

if __name__ == '__main__':
    print(Solution.findLongestSubarray(self=None,
                                       array=["A", "B", "C", "D"]))
