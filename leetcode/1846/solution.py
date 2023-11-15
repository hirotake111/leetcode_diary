"""
https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/
1864. Maximum Element After Decreasing and Rearranging
"""


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        answer = 1
        for i in range(1, len(arr)):
            answer = min(answer + 1, arr[i])
        return answer
