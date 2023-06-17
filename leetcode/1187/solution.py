"""
https://leetcode.com/problems/make-array-strictly-increasing/
1187. Make Array Strictly Increasing

Given two integer arrays arr1 and arr2, return the minimum number of operations (possibly zero) needed to make arr1 strictly increasing.
In one operation, you can choose two indices 0 <= i < arr1.length and 0 <= j < arr2.length and do the assignment arr1[i] = arr2[j].
If there is no way to make arr1 strictly increasing, return -1.
"""
from typing import List, Tuple
from unittest import TestCase, main
from bisect import bisect_right
from functools import lru_cache


class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        MAX = 10**9 + 1
        arr2 = sorted(set(arr2))

        @lru_cache(None)
        def dfs(i, prev):
            if i >= len(arr1):
                return 0
            j = bisect_right(arr2, prev)
            do_nothing = dfs(i + 1, arr1[i]) if prev < arr1[i] else MAX
            swap = 1 + dfs(i + 1, arr2[j]) if j < len(arr2) else MAX
            return min(swap, do_nothing)

        changes = dfs(0, -1)
        return changes if changes != MAX else -1
