// 1143. Longest Common Subsequence
// https://leetcode.com/problems/longest-common-subsequence/description/
package lc1143

/*
	This is a classic DP problem
	text1 = "abcde", text2 = "ace"
	1. Since the 1st chars are the same (= "a"), we can break it down to a subproblem.
	-> text1 = "bcde", text2 = "ce" + 1
	2. The next 2 chars aren't the same ("b", "c"), let's divide it into 2 subproblem.
	-> text1 = "cde", text2 = "ce" + 1, or
	-> text1 = "bcde", text2 = "c" + 1
	2-1. The next 2 chars are the same ("c")
	-> text1 = "de", text2 = "e" + 1 + 1
	3. The next 2 chars are not ("d", "e"), so let's divide it in to 2 subproblem.
	-> text1 = "de", text2 = "" + 1 + 1, or
	-> text1 = "e", text2 = "e" + 1 + 1
	3-2. The next 2 chars are the same ("e")
	-> 1 + 1 + 1
	4. With this approach we can start from the last to fist indexes, using DP.
*/

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func longestCommonSubsequence(text1 string, text2 string) int {
	m, n := len(text1), len(text2)
	// Initialize dp array (slice)
	dp := make([][]int, m+1)
	for i := 0; i < m+1; i++ {
		dp[i] = make([]int, n+1)
		for j := 0; j < n+1; j++ {
			dp[i][j] = 0
		}
	}

	// Start from the 2nd last character
	for i := m - 1; 0 <= i; i-- {
		for j := n - 1; 0 <= j; j-- {
			if text1[i] == text2[j] {
				dp[i][j] = dp[i+1][j+1] + 1
			} else {
				dp[i][j] = max(dp[i][j+1], dp[i+1][j])
			}
		}
	}

	return dp[0][0]
}
