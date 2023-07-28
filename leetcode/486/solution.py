"""
https://leetcode.com/problems/predict-the-winner/
486. Predict the Winner
"""
from typing import List
from functools import lru_cache


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        @lru_cache(None)
        def dfs(i: int, j: int) -> int:
            if i + 1 == j:
                return abs(nums[i] - nums[j])

            return max(nums[i] - dfs(i + 1, j), nums[j] - dfs(i, j - 1))

        return dfs(0, len(nums) - 1) >= 0
