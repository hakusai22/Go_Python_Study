package _024_01

/*
   --idea
   -*- coding: utf-8 -*-
   @Author  : hakusai22
   @Time    : 2024/01/02 23:09
*/

func minOperationsMaxProfit(customers []int, boardingCost int, runningCost int) int {
	ans := -1
	t, mx := 0, 0
	wait, i := 0, 0
	for wait > 0 || i < len(customers) {
		if i < len(customers) {
			wait += customers[i]
		}
		up := min(4, wait)
		wait -= up
		t += up*boardingCost - runningCost
		i++
		if t > mx {
			mx = t
			ans = i
		}
	}
	return ans
}
