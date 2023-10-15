"""
https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/
1269. Number of Ways to Stay in the Same Place After Some Steps
"""


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 1000000007

        @lru_cache(None)
        def dfs(i: int, steps: int) -> int:
            if i < 0 or arrLen <= i:
                return 0
            if steps == 0:
                return 1 if i == 0 else 0
            return (
                dfs(i - 1, steps - 1) + dfs(i, steps - 1) + dfs(i + 1, steps - 1)
            ) % MOD

        return dfs(0, steps) % MOD
