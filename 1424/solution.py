"""
https://leetcode.com/problems/diagonal-traverse-ii/
1424. Diagonal Traverse II
"""
from typing import List


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        longest = max(len(arr) for arr in nums)
        tmp = [[] for _ in range(len(nums) + longest - 1)]

        for i, arr in enumerate(nums):
            for j, n in enumerate(arr):
                tmp[i + j].append(n)

        return [n for arr in tmp for n in arr[::-1]]
