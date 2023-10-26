"""
https://leetcode.com/problems/binary-trees-with-factors/
823. Binary Trees With Factors
"""
from type import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """Optimized Solution"""
        arr.sort()
        MOD = 10**9 + 7
        dp = {n: 1 for n in arr}

        for i, parent in enumerate(arr):
            for i in range(i):
                if parent % arr[i] == 0 and parent // arr[i] in dp:
                    dp[parent] = (dp[parent] + dp[arr[i]] * dp[parent // arr[i]]) % MOD
        return sum(dp.values()) % MOD


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        """Initial Approach (Recursive Function)"""
        s = set(arr)
        total = 0
        MOD = 10**9 + 7

        @lru_cache(None)
        def dfs(parent: int) -> int:
            total = 1  # [n]
            for left in arr:
                right, r = divmod(parent, left)
                if r == 0 and right in s:
                    total = total + (dfs(left) * dfs(right)) % MOD
            return total

        return sum(dfs(n) for n in arr) % MOD
