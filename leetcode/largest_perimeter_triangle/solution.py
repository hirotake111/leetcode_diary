from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            first, second, third = nums[i : i + 3]
            if first < (second + third):
                return sum(nums[i : i + 3])

        return 0
