"""
https://leetcode.com/problems/longest-arithmetic-subsequence-of-given-difference/
1218. Longest Arithmetic Subsequence of Given Difference

Given an integer array arr and an integer difference, return the length of the longest subsequence in arr which is an arithmetic sequence such that the difference between adjacent elements in the subsequence equals difference.

A subsequence is a sequence that can be derived from arr by deleting some or no elements without changing the order of the remaining elements.
"""
from typing import List, Dict


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp: Dict[int, int] = {}
        longest = 0

        for n in arr:
            prev_value = n - difference
            value = dp.get(prev_value, 0) + 1
            dp[n] = value
            longest = max(longest, value)

        return longest
