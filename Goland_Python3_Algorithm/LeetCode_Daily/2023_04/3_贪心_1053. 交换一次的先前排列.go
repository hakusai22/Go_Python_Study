package _023_04

/*
   -*- coding: utf-8 -*-
   @Author  : wheat
   @Time    : 2023/04/03 09:16
*/

func prevPermOpt1(arr []int) []int {
	n := len(arr)
	for i := n - 1; i > 0; i-- {
		if arr[i-1] > arr[i] {
			for j := n - 1; j > i-1; j-- {
				if arr[j] < arr[i-1] && arr[j] != arr[j-1] {
					arr[i-1], arr[j] = arr[j], arr[i-1]
					return arr
				}
			}
		}
	}
	return arr
}
