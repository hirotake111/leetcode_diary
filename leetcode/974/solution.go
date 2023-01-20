/*
https://leetcode.com/problems/subarray-sums-divisible-by-k/
974. Subarray Sums Divisible by K

Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.
*/
package main

func subarraysDivByK(nums []int, k int) int {
	prefixSums := make(map[int]int)
	prefixSums[0] = 1
	answer, sum := 0, 0

	for _, n := range nums {
		sum = (((sum + nums[n]) % k) + k) % k
		counts := prefixSums[sum]
		answer += counts
		prefixSums[sum]++
	}
	return answer
}

func abs(a int) int {
	if a < 0 {
		return a * -1
	}
	return a

}
