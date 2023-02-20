"""
https://leetcode.com/problems/search-insert-position/description/
35. Search Insert Position
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1

        while True:
            if target <= nums[low]:
                return low
            if target == nums[high]:
                return high
            if nums[high] < target:
                return high + 1
            if low + 1 == high:
                return high

            mid = (high - low) // 2 + low
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                high = mid - 1
                if low == high:
                    # low < target < mid
                    return mid
            elif nums[mid] < target:
                low = mid + 1
                if low == high:
                    # mid < target < high
                    return high
