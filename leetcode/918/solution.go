/*
https://leetcode.com/problems/maximum-sum-circular-subarray/
918. Maximum Sum Circular Subarray

Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
*/
package main

func maxSubarraySumCircular(nums []int) int {
	answer := nums[0]
	summary := sum(&nums)
	maximum := max(nums[0], nums...)

	// Short cuts
	if 0 < min(nums[0], nums...) {
		return summary
	}
	if maximum < 0 {
		return maximum
	}

	total := 0
	for _, v := range nums {
		if total < 0 {
			total = 0
		}
		total += v
		answer = max(answer, total)
	}
	total = 0
	for _, v := range nums {
		if 0 < total {
			total = 0
		}
		total += v
		answer = max(answer, summary-total)
	}

	return answer
}

func sum(arr *[]int) int {
	summary := 0
	for _, n := range *arr {
		summary += n
	}
	return summary
}

func min(a int, b ...int) int {
	minimum := a
	for _, c := range b {
		if c < minimum {
			minimum = c
		}
	}
	return minimum
}

func max(a int, b ...int) int {
	maximum := a
	for _, c := range b {
		if maximum < c {
			maximum = c
		}
	}
	return maximum
}
