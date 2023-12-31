"""
https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
1335. Minimum Difficulty of a Job Schedule
"""
from functools import lru_cache


class Solution:
    def minDifficulty(self, arr: List[int], d: int) -> int:
        @lru_cache(None)
        def dfs(i: int, extra_days: int, max_val: int) -> int:
            if i == len(arr):
                return 300 * 1000 + 1  # possible maximum value
            if extra_days == 0:
                return max(max_val, max(arr[i:]))
            max_val = max(max_val, arr[i])
            next_day = max_val + dfs(i + 1, extra_days - 1, 0)
            same_day = dfs(i + 1, extra_days, max_val)
            return min(next_day, same_day)

        # edge cases
        if len(arr) < d:
            return -1
        if d == 1:
            return max(arr)
        if all(map(lambda x: x == 0, arr)):
            return 0

        return dfs(0, d - 1, 0)
