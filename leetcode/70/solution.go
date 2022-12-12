// 70. Climbing Stairs
// https://leetcode.com/problems/climbing-stairs/
package lc70

func climbStairs(n int) int {
	// Initialize slice dp with 0 (we need it with the length of n+1 )
	dp := make([]int, n+1)
	i := 0
	for i < n {
		dp[i] = 0
		i++
	}

	var dfs func(x int) int
	dfs = func(x int) int {
		// If x is 1 or 2, just return it.
		if x <= 2 {
			return x
		}
		// If we have already populate x, then return it.
		if 0 < dp[x] {
			return dp[x]
		}
		// Now x is greater than 2 and we don't have the result of dp[x].
		// Populate result first and then return it.
		dp[x] = dfs(x-2) + dfs(x-1)
		return dp[x]

	}

	return dfs(n)
}
