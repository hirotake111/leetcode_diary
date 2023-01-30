/*
https://leetcode.com/problems/n-th-tribonacci-number/
1137. N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
*/
package main

func tribonacci(n int) int {
	arr := []int{0, 1, 1}
	if n < 3 {
		return arr[n]
	}
	for i := 3; i <= n; i++ {
		arr[i%3] = arr[0] + arr[1] + arr[2]
	}

	return arr[n%3]
}
