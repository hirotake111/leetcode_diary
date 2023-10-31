/*
https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
2433. Find the Original Array of Prefix Xor
*/
package main

func findArray(pref []int) []int {
	arr := make([]int, len(pref))
	arr[0] = pref[0]
	for i := 1; i < len(pref); i++ {
		arr[i] = pref[i] ^ pref[i-1]
	}
	return arr
}
