/**
 * https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
 * 1846. Maximum Element After Decreasing and Rearranging
 */

package main

import "sort"

func maximumElementAfterDecrementingAndRearranging(arr []int) int {
	sort.Ints(arr)
	answer := 1
	for i := 1; i < len(arr); i++ {
		if answer < arr[i] {
			answer += 1
		}
	}
	return answer
}
