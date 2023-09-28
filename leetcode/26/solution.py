"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
26. Remove Duplicates from Sorted Array
"""
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i, prev = 0, -101
        for c in nums:
            if prev < c:
                nums[i] = prev = c
                i += 1
        return i 


