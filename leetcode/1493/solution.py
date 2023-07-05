"""
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/
1493. Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
"""
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        """Sliding window approach"""
        slow, skip = 0, 1
        answer = 0
        for fast in range(len(nums)):
            if nums[fast] == 0:
                skip -= 1
            while skip < 0:
                if nums[slow] == 0:
                    skip += 1
                slow += 1
            answer = max(answer, fast - slow)

        return answer

        """
        My initial approach (without using sliding window approach, but two pointers)
        The idea is we iterate over and array and find an island of ones.
        Then if the subsequent zeros are only one, we store the result to "prev" for later use (otherwise, store 0).
        And every time we found a new island of ones, we compare the current maximum value and (result + prev)
        """
        # i = prev = answer = 0
        # if sum(nums) == len(nums):
        # # You must delete one element
        # return len(nums) - 1

        # # Find the 1st "1"
        # while i < len(nums):
        # if nums[i] == 1:
        # break
        # i += 1

        # while i < len(nums):
        # # Find next 0
        # j = i + 1
        # while j < len(nums):
        # if nums[j] == 0:
        # break
        # j += 1

        # ones = len(nums[i:j])
        # answer = max(answer, prev + ones)
        # # Now j points to either "0", or out of bound
        # if j >= len(nums) - 1:
        # # No longer need to find i
        # break

        # i = j + 1
        # if nums[i] == 1:
        # # We can combine this 1s and next 1s -> store current state
        # prev = ones
        # else:
        # # Cannot combine -> reset prev
        # prev = 0
        # # And find next starting index
        # while i < len(nums):
        # if nums[i] == 1:
        # break
        # i += 1

        # return answer
