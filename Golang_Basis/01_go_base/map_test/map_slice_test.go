package _09_map

/*
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2023/08/13 23:36
*/

import (
	"fmt"
	"testing"
)

func TestSlice(t *testing.T) {
	main5()
}

func main5() {

	//要求：使用一个map来记录monster的信息 name 和 age, 也就是说一个monster对应一个map,并且妖怪的个数可以动态的增加=>map切片
	//1. 声明一个map切片
	var monsters []map[string]string
	monsters = make([]map[string]string, 2) //准备放入两个妖怪

	//2. 增加妖怪的信息
	if monsters[0] == nil {
		monsters[0] = make(map[string]string, 2)
		monsters[0]["name"] = "牛魔王"
		monsters[0]["age"] = "500"
	}

	if monsters[1] == nil {
		monsters[1] = make(map[string]string, 2)
		monsters[1]["name"] = "玉兔精"
		monsters[1]["age"] = "400"
	}

	// 下面这个写法越界。
	// if monsters[2] == nil {
	// 	monsters[2] = make(map[string_test]string_test, 2)
	// 	monsters[2]["name"] = "狐狸精"
	// 	monsters[2]["age"] = "300"
	// }

	//使用到切片的append函数，可以动态的增加monster
	//3. 先定义个monster信息
	newMonster := map[string]string{
		"name": "新的妖怪~火云邪神",
		"age":  "200",
	}
	monsters = append(monsters, newMonster)

	fmt.Println(monsters)
}
