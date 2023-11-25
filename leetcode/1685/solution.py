"""
https://leetcode.com/problems/sum-of-absolute-differences-in-a-sorted-array/
1685. Sum of Absolute Differences in a Sorted Array
"""
from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        left = 0
        right = sum(nums)
        j = len(nums)

        for i, n in enumerate(nums):
            answer[i] = right - left + n * (i - j)
            left += n
            right -= n
            j -= 1

        return answer
