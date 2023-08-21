"""
https://leetcode.com/problems/3sum-closest/
16. 3Sum Closest
"""
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        """two pointer approach"""
        nums.sort()
        n = len(nums)
        result = 100001

        for base in range(n - 1):
            if 0 < base and nums[base] == nums[base - 1]:
                continue

            left, right = base + 1, n - 1
            while left < right:
                total = nums[base] + nums[left] + nums[right]
                if abs(target - total) < abs(target - result):
                    result = total
                if target <= total:
                    prev = nums[right]
                    while left < right and prev == nums[right]:
                        right -= 1
                else:
                    prev = nums[left]
                    while left < right and prev == nums[left]:
                        left += 1

        return result
