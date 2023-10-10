"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/?envType=daily-question&envId=2023-10-10
2009. Minimum Number of Operations to Make Array Continuous
"""
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l = len(nums)
        # Remove duplicated elements to make the problem simple
        nums = list(set(nums))

        # Shortcut
        if max(nums) - min(nums) <= l - 1:
            # Add duplicated elements to the answer
            return 0 + (l - len(nums))

        nums.sort()
        min_ops = 100001

        i = 0
        for j, n in enumerate(nums):
            # Move i until we meet the condition (nums[j] - nums[i] <= boundary)
            while i < j and n - nums[i] > l - 1:
                i += 1
            num_of_elements = j - i + 1
            ops_needed = len(nums) - num_of_elements
            min_ops = min(min_ops, ops_needed)

        return min_ops + (l - len(nums))
