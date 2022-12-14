"""
198. House Robber
https://leetcode.com/problems/house-robber/
"""
from typing import List
from functools import lru_cache


class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        @lru_cache()
        def dfs(m: int) -> int:
            if n <= m:  # out of bound -> return 0
                return 0
            # Else, pick up either  m+2 and m+3
            return nums[m] + max(dfs(m + 2), dfs(m + 3))

        if n == 1:  # Only one element in nums -> return it
            return nums[0]

        # Start with index 0 and 1, then return greater one
        return max(dfs(0), dfs(1))
