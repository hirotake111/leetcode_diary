/*
https://leetcode.com/problems/n-th-tribonacci-number/
1137. N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
*/
package main

func tribonacci(n int) int {
	if n == 0 {
		return 0
	}
	if n <= 2 {
		return 1
	}
	a, b, c, d := 0, 1, 1, 0
	for 2 < n {
		a = b
		b = c
		c = d
		d = a + b + c
		n--
	}
	return d

}
