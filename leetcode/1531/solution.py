"""
https://leetcode.com/problems/string-compression-ii/
1531. String Compression II
"""
from functools import lru_cache


class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        @lru_cache(None)
        def dfs(i: int, k: int, prev: str, prev_cnt: int) -> int:
            if k < 0:
                return float("inf")
            if i == len(s):
                return 0
            if s[i] == prev:
                inc = 1 if prev_cnt in [1, 9, 99] else 0
                return inc + dfs(i + 1, k, prev, prev_cnt + 1)
            return min(dfs(i + 1, k - 1, prev, prev_cnt), 1 + dfs(i + 1, k, s[i], 1))

        return dfs(0, k, "", 0)
