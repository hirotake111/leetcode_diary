"""
https://leetcode.com/problems/interleaving-string/
97. Interleaving String
"""
from functools import lru_cache


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        m, n = len(s1), len(s2)

        if m + n != len(s3):
            return False

        @lru_cache(None)
        def dfs(i: int, j: int) -> bool:
            if i == m:
                # Compare the rest of s2 and s3
                return s2[j:] == s3[i + j :]
            if j == n:
                # Compare the rest of s1 and s3
                return s1[i:] == s3[i + j :]

            target = s3[i + j]
            if s1[i] == s2[j] == target:
                return dfs(i + 1, j) or dfs(i, j + 1)
            elif s1[i] == target:
                return dfs(i + 1, j)
            elif s2[j] == target:
                return dfs(i, j + 1)
            else:
                return False

        return dfs(0, 0)
