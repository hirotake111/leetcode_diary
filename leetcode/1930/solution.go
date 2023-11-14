/**
 * https://leetcode.com/problems/unique-length-3-palindromic-subsequences/
 * 1930. Unique Length-3 Palindromic Subsequences
 */
package main

func countPalindromicSubsequence(s string) int {
	b := []rune(s)
	letters := make(map[rune]bool)

	// find out unique characters
	for _, c := range b {
		letters[c] = true
	}

	total := 0
	for c := range letters {
		l := -1
		r := 0
		// identify left-most index and right-most index of s
		for i := 0; i < len(b); i++ {
			if b[i] == c {
				r = i
				if l == -1 {
					l = i
				}
			}
		}
		if r-l >= 2 {
			uq := make(map[rune]bool)
			for _, c := range b[l+1 : r] {
				uq[c] = true
			}
			total += len(uq)
		}
	}
	return total
}
