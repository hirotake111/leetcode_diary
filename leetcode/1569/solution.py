"""
https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/
1569. Number of Ways to Reorder Array to Get Same BST
"""
from typing import List
from math import comb


class Solution:
    def numOfWays(self, nums: List[int]) -> int:
        MOD = 10**9 + 7

        def dfs(arr: List[int]) -> int:
            if len(arr) < 2:
                return 1
            left = [x for x in arr if x < arr[0]]
            right = [x for x in arr if x > arr[0]]

            return comb(len(left) + len(right), len(right)) * dfs(left) * dfs(right)

        return (dfs(nums) - 1) % MOD
