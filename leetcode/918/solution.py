"""
https://leetcode.com/problems/maximum-sum-circular-subarray/
918. Maximum Sum Circular Subarray

Given a circular integer array nums of length n, return the maximum possible sum of a non-empty subarray of nums.

A circular array means the end of the array connects to the beginning of the array. Formally, the next element of nums[i] is nums[(i + 1) % n] and the previous element of nums[i] is nums[(i - 1 + n) % n].

A subarray may only include each element of the fixed buffer nums at most once. Formally, for a subarray nums[i], nums[i + 1], ..., nums[j], there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        answer, summary = nums[0], sum(nums)

        # short cuts
        if 0 <= min(nums):
            return summary
        elif max(nums) <= 0:
            return max(nums)

        total = 0
        for v in nums:
            total = max(total, 0) + v
            answer = max(answer, total)

        # Instead of seeing nums as circular array,
        # let's find a minimum subarray
        total = 0
        for v in nums:
            total = min(total, 0) + v
            answer = max(answer, summary - total)

        return answer


class Test(TestCase):
    data: List[Tuple[List[int], int]] = [
        ([5, -3, 5], 10),
    ]

    def test_solution(self):
        s = Solution()
        for nums, expected in self.data:
            self.assertEqual(s.maxSubarraySumCircular(nums), expected)


if __name__ == "__main__":
    main()
