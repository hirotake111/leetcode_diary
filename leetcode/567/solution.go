/*
https://leetcode.com/problems/permutation-in-string/
567. Permutation in String

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
*/
package main

func checkInclusion(s1 string, s2 string) bool {
	if len(s2) < len(s1) {
		return false
	}

	// Sliding window approach
	arr1, arr2 := make([]int, 26), make([]int, 26)
	// Populate frequency of s1 and s2
	for i, c1 := range s1 {
		c2 := s2[i]
		arr1[c1-97]++
		arr2[c2-97]++
	}
	if compare(arr1, arr2) {
		return true
	}

	for i := 0; i < len(s2)-len(s1); i++ {
		newIdx := i + len(s1)
		oldCh := s2[i]
		newCh := s2[newIdx]
		// Update frequency of s2
		arr2[oldCh-97]--
		arr2[newCh-97]++
		// Compare frequencies
		if compare(arr1, arr2) {
			return true
		}
	}
	return false

}

func compare(a, b []int) bool {
	for i, n := range a {
		if n != b[i] {
			return false
		}
	}
	return true
}
