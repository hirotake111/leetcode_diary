"""
https://leetcode.com/problems/permutations/
46. Permutations
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]
        if len(nums) == 1:
            return [nums]
        if len(nums) == 2:
            a, b = nums
            return [[a, b], [b, a]]

        arr = []
        for i in range(len(nums)):
            n = nums[i]
            nums_without_n = nums[:i] + nums[i + 1 :]
            for sub_arr in self.permute(nums_without_n):
                arr.append([n] + sub_arr)

        return arr
