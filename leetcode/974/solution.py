"""
https://leetcode.com/problems/subarray-sums-divisible-by-k/
974. Subarray Sums Divisible by K

Given an integer array nums and an integer k, return the number of non-empty subarrays that have a sum divisible by k.

A subarray is a contiguous part of an array.
"""
from typing import List, DefaultDict
from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Maintain previous prefix sums
        prefix_sums: DefaultDict[int, int] = defaultdict(int)
        prefix_sums[0] = 1
        sum, answer = 0, 0

        for n in nums:
            sum += n
            reminder = sum % k
            # Add the count of prefix sums
            answer += prefix_sums[reminder]
            prefix_sums[reminder] += 1

        return answer
