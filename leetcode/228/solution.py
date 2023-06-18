"""
https://leetcode.com/problems/summary-ranges/

228. Summary Ranges

You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b
"""
from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        answer = []

        # Edge case
        if len(nums) == 0:
            return []

        a = b = nums[0]
        for n in nums[1:]:
            if n == b + 1:
                b = n
                continue
                # If this is the last element in nums, then...
                # a != b
                # b == n

            if a == b:
                answer.append(f"{a}")
            else:
                answer.append(f"{a}->{b}")
            # nums[i] should be the next "a"
            a = b = n
            # If this is the last element in nums, then...
            # a == b == n

        if a == b:
            answer.append(f"{a}")
        else:
            answer.append(f"{a}->{b}")
        return answer
