package main

import (
	"fmt"
	"sort"
)

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/08/13 23:34
*/

// map是无序的
func main() {

	//map的排序
	map1 := make(map[int]int, 10)
	map1[10] = 100
	map1[1] = 13
	map1[4] = 56
	map1[8] = 90
	fmt.Println(map1)

	//如果按照map的key的顺序进行排序输出
	//1. 先将map的key 放入到 切片中
	//2. 对切片排序
	//3. 遍历切片，然后按照key来输出map的值
	var keys []int
	for k, _ := range map1 {
		keys = append(keys, k)
	}

	//Sorting
	sort.Ints(keys)
	fmt.Println(keys)

	for _, k := range keys {
		fmt.Printf("map1[%v]=%v \n", k, map1[k])
	}

}
