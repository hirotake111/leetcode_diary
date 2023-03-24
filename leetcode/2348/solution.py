"""
https://leetcode.com/problems/number-of-zero-filled-subarrays/
2348. Number of Zero-Filled Subarrays
Given an integer array nums, return the number of subarrays filled with 0.

A subarray is a contiguous non-empty sequence of elements within an array.
"""
from typing import List

"""
- How many we have in given array? -
It's a simple math. Consider an array with 4 elements. There are:
subarray with 1 element: 4
subarray with 2 elements: 3
subarray with 3 elements: 2
subarray with 4 elements: 1
Overall you just increment count by 1 and finally add it to the answer
"""


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        answer = count = 0
        for n in nums:
            if n == 0:
                count += 1
                answer += count
            else:
                count = 0
        return answer
