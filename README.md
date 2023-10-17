# Go_Python_Study

Go_Python_Study 学习记录

<!-- PROJECT SHIELDS -->

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![MIT License][license-shield]][license-url]
![GitHub top language](https://img.shields.io/github/languages/top/hakusai22/Go_Python_Study?style=for-the-badge)

<!-- PROJECT LOGO -->
<br />



<p align="center">
    <a href="https://github.com/hakusai22/Go_Python_Study/">
    </a>
    <h3 align="center">Go_Python 算法学习笔记 🔞</h3>
  <p align="center">
    ·
    <a href="https://github.com/hakusai22/Go_Python_Study/issues">报告Bug</a>
    ·
    <a href="https://github.com/hakusai22/Go_Python_Study/issues">提出新特性</a>
  </p>


<img src="https://fastly.jsdelivr.net/gh/hakusai22/Go_Python_Study/al.png"/>
<img src="https://fastly.jsdelivr.net/gh/hakusai22/Go_Python_Study/code_language.png"/>

<!-- links -->

[your-project-path]:hakusai22/Go_Python_Study

[contributors-shield]: https://img.shields.io/github/contributors/hakusai22/Go_Python_Study.svg?style=for-the-badge

[contributors-url]: https://github.com/hakusai22/Go_Python_Study/graphs/contributors

[forks-shield]: https://img.shields.io/github/forks/hakusai22/Go_Python_Study.svg?style=for-the-badge

[forks-url]: https://github.com/hakusai22/Go_Python_Study/network/members

[stars-shield]: https://img.shields.io/github/stars/hakusai22/Go_Python_Study.svg?style=for-the-badge

[stars-url]: https://github.com/hakusai22/Go_Python_Study/stargazers

[issues-shield]: https://img.shields.io/github/issues/hakusai22/Go_Python_Study.svg?style=for-the-badge

[issues-url]: https://img.shields.io/github/issues/hakusai22/Go_Python_Study.svg

[license-shield]: https://img.shields.io/github/license/hakusai22/Go_Python_Study.svg?style=for-the-badge

[license-url]: https://github.com/hakusai22/Go_Python_Study/blob/master/LICENSE

[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555

[linkedin-url]: https://linkedin.com/in/xxxx

## 项目目录
- [Algorithm](#Algorithm)
  - [Python3/Go算法模版总结](#算法模版总结)
- [Goland_Grammar](#Goland_Grammar)
  - [Go语法](#Go语法)
- [Middleware](#Middleware)
  - [Go中间件](#Go中间件)
- [Python3_Grammar](#Python3_Grammar)
  - [Python3语法](#Python3语法)

## 目录

- [上手指南](#上手指南)
    - [开发前的配置要求](#开发前的配置要求)
    - [安装步骤](#安装步骤)
- [文件目录说明](#文件目录说明)
- [项目特点](#项目特点)
- [功能介绍](#功能介绍)
- [开发的架构](#开发的架构)
- [部署](#部署)
- [使用到的框架](#使用到的框架)
- [贡献者](#贡献者)
    - [如何参与开源项目](#如何参与开源项目)
- [版本控制](#版本控制)
- [作者](#作者)
- [鸣谢](#鸣谢)
- [成果演示](#成果演示)

### 上手指南

###### 开发前的配置要求

###### **安装步骤**

### 项目特点


```bash
go mod init	生成 go.mod 文件
go mod download	下载 go.mod 文件中指明的所有依赖
go mod tidy	整理现有的依赖
go mod graph	查看现有的依赖结构
go mod edit	编辑 go.mod 文件
go mod vendor	导出项目所有的依赖到vendor目录
go mod verify	校验一个模块是否被篡改过
go mod why	查看为什么需要依赖某模块
```

### 分类型刷题

#### 基础数据结果
- [链表](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Linked_List)
- [位运算](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Bit_Operations/位运算.md)
- [哈希表](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Hash_Table)
- [递归](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Recursion)
- [贪心][Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Greedy]
- [排序][Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Sorting]
- [字符串](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Strings)
- [双指针算法](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Two_Pointer)
- [滑动窗口](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Sliding_Window)
- [栈&&单调栈](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Stack)
- [队列&&单调队列](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Queue)
- [大根堆&&小根堆](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Heap/堆.md)
- [二叉树](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Binary_Tree)
- [贪心算法](https://github.com/hakusai22/Go_Python_Study#贪心算法)
- [动态规划](Algorithm/Algorithm_Questions_By_Tags/Dynamic_Programming)
- [二分搜索](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Binary_Search/二分查找.md)
- [前缀和&&差分数组](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Prefix_Sum/前缀和.md)
- [字典树](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Trie_Tree)
- [并查集](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Union_Find/并查集.md)
- [树状数组](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Fenwick_Tree)
- [线段树](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Segment_Tree/线段树.md)
- [区间操作](Algorithm/Algorithm_Questions_By_Tags/Data_Structure/Interval_Merging)


#### 动态规划
- [记忆化搜索](Algorithm/Algorithm_Questions_By_Tags/Dynamic_Programming/Memory_Search)
- [线性DP](Algorithm/Algorithm_Questions_By_Tags/Dynamic_Programming/Linear_DP)
- [背包DP](Algorithm/Algorithm_Questions_By_Tags/Dynamic_Programming/Backpack_DP)
- [状压DP](Algorithm/Algorithm_Questions_By_Tags/Dynamic_Programming/State_Compression_DP)
- [区间DP](Algorithm/Algorithm_Questions_By_Tags/Dynamic_Programming/Interval_DP)
- [计数DP](Algorithm/Algorithm_Questions_By_Tags/Dynamic_Programming/Count_DP)
- [树形DP](Algorithm/Algorithm_Questions_By_Tags/Dynamic_Programming/Tree_Shape_DP)

#### 搜索
- [DFS]()
- [BFS]()
- [双向搜索]()
- [回溯]()
- [A*]()

#### 图论
- [DFS图论](Algorithm/Algorithm_Questions_By_Tags/Graph/DFS)
- [BFS图论](Algorithm/Algorithm_Questions_By_Tags/Graph/BFS)
- [拓扑排序](Algorithm/Algorithm_Questions_By_Tags/Graph/Topological_Sorting)
- [最小生成树]
  - [Kruskal 算法](Algorithm/Algorithm_Questions_By_Tags/Graph/Kruskal)
  - [Prim 算法](Algorithm/Algorithm_Questions_By_Tags/Graph/Prim)
- [最短路]
  - [Floyd 算法](Algorithm/Algorithm_Questions_By_Tags/Graph/Floyd)
  - [Bellman–Ford 算法](Algorithm/Algorithm_Questions_By_Tags/Graph/Bellman_Ford)
  - [Dijkstra 算法](Algorithm/Algorithm_Questions_By_Tags/Graph/Dijkstra)

#### 数学
- [约数](Algorithm/Algorithm_Questions_By_Tags/Mathematical_Knowledge/Divisor)
- [质数](Algorithm/Algorithm_Questions_By_Tags/Mathematical_Knowledge/Prime_Number)
- [快速幂](Algorithm/Algorithm_Questions_By_Tags/Mathematical_Knowledge/Fast_Exponentiation)
- [组合数](Algorithm/Algorithm_Questions_By_Tags/Mathematical_Knowledge/Combinations)
- [容斥原理](Algorithm/Algorithm_Questions_By_Tags/Mathematical_Knowledge/Inclusion_Exclusion_Principle)