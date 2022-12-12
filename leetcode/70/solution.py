"""
70. Climbing Stairs
https://leetcode.com/problems/climbing-stairs/
"""
from functools import lru_cache


class Solution:
    def climbStairs(self, n: int) -> int:
        @lru_cache()
        def dfs(x: int) -> int:
            if x == 1:  # we have only 1 pattern (that is, [1])
                return 1
            if x == 2:  # we have only 2 patterns ([1,1] and [2])
                return 2
            # otherwise, search and combine the result of n - 2 and n - 1
            return dfs(x - 2) + dfs(x - 1)

        return dfs(n)
