"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/submissions/
34. Find First and Last Position of Element in Sorted Array
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        answer = [-1, -1]
        if len(nums) == 0 or target < nums[0] or nums[-1] < target:
            return answer

        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if target <= nums[m]:
                r = m
            else:  # nums[m] < target
                l = m + 1

        if nums[l] != target:
            return [-1, -1]

        answer[0] = l
        r = len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] <= target:
                l = m + 1
            else:  # target < nums[m]
                r = m

        answer[1] = r if nums[r] == target else r - 1
        return answer


"""
# Optimized version:
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0 or target < nums[0]  or nums[-1] < target:
            return [-1, -1]

        l = bisect_left(nums, target)
        if nums[l] != target:
           return [-1, -1] 
        r = bisect_right(nums, target)
        
        return [l, r - 1] if r == len(nums) or nums[r] != target else [l, r]
"""
