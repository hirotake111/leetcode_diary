/**
 * https://leetcode.com/problems/count-number-of-homogenous-substrings/
 * 1759. Count Number of Homogenous Substrings
 */
package main

func countHomogenous(s string) int {
	total, count := 1, 1
	MOD := 1_000_000_007
	for i := 1; i < len(s); i++ {
		if s[i] == s[i-1] {
			count = (count + 1) % MOD
		} else {
			count = 1
		}
		total = (total + count) % MOD
	}
	return total
}
