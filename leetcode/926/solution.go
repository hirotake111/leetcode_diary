/*
https://leetcode.com/problems/flip-string-to-monotone-increasing/
926. Flip String to Monotone Increasing

A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.
*/
package main

func minFlipsMonoIncr(s string) int {
	var answer int
	i := -1
	for idx, c := range s {
		if c == '1' {
			i = idx
			break
		}
	}
	if i == -1 { // all digits are zeroes
		return 0
	}

	// Ignore all zeroes on the left size
	s = s[i:]

	left := 0
	right := 0
	// count num of zeroes
	for _, c := range s {
		if c == '0' {
			right++
		}
	}
	answer = right

	for _, c := range s {
		if c == '1' { // increment left
			left++
		} else { // '0' -> decrement right
			right--
		}
		// Compare left+right and answer
		if left+right < answer {
			answer = left + right
		}
	}
	return answer
}
