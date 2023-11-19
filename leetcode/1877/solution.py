"""
https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
1977. Minimize Maximum Pair Sum in Array
"""


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max([nums[i] + nums[-i - 1] for i in range(len(nums) // 2)])
