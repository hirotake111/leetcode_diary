"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/?envType=daily-question&envId=2023-10-10
2009. Minimum Number of Operations to Make Array Continuous
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l = len(nums)
        boundary = l - 1
        # remove duplicated elements to make the problem easier
        nums = sorted(set(nums))
        min_ops = 100001

        # Shortcut
        if max(nums) - min(nums) <= boundary:
            return 0 + (l - len(nums))

        i = j = 0
        while j < len(nums):
            # Move i until we meet the condition (nums[j] - nums[i] <= boundary)
            while i < j and nums[j] - nums[i] > boundary:
                i += 1
            num_of_elements = j - i + 1
            ops_needed = len(nums) - num_of_elements
            min_ops = min(min_ops, ops_needed)
            j += 1

        return min_ops + (l - len(nums))
