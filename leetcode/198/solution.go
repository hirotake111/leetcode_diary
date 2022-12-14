// 198. House Robber
// https://leetcode.com/problems/house-robber/description/
package lc198

func max(a, b int) int {
	if a < b {
		return b
	}
	return a
}

func rob(nums []int) int {
	n := len(nums)
	var dfs func(m int) int
	dp := make([]int, n)

	// Initialize dp with -1
	for i := range dp {
		dp[i] = -1
	}

	dfs = func(m int) int {
		if n <= m { // Out fo bound -> return 0
			return 0
		}
		if dp[m] != -1 { // We already know the result -> return it
			return dp[m]
		}
		// Then recursively call dfs and store it to dp
		dp[m] = nums[m] + max(dfs(m+2), dfs(m+3))
		return dp[m]
	}

	if n == 1 {
		return nums[0]
	}

	// Start with index 0 and 1, then return greater one
	return max(dfs(0), dfs(1))
}
