"""
https://leetcode.com/problems/k-radius-subarray-averages/description/
2090. K Radius Subarray Averages

You are given a 0-indexed array nums of n integers, and an integer k.
The k-radius average for a subarray of nums centered at some index i with the radius k is the average of all elements in nums between the indices i - k and i + k (inclusive). If there are less than k elements before or after the index i, then the k-radius average is -1.
Build and return an array avgs of length n where avgs[i] is the k-radius average for the subarray centered at index i.
The average of x elements is the sum of the x elements divided by x, using integer division. The integer division truncates toward zero, which means losing its fractional part.
For example, the average of four elements 2, 3, 1, and 5 is (2 + 3 + 1 + 5) / 4 = 11 / 4 = 2.75, which truncates to 2.
"""
from typing import List


class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = k * 2 + 1  # length from i - k to i + k (inclusive)
        avgs = [-1] * len(nums)
        total = sum(nums[: k * 2])

        for i in range(k, len(nums) - k):
            total += nums[i + k]
            avgs[i] = total // n
            total -= nums[i - k]

        return avgs
