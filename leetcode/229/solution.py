"""
https://leetcode.com/problems/majority-element-ii/
229. Majority Element II
"""
from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        threshold = len(nums) // 3
        arr = []
        for n, count in Counter(nums).items():
            if count > threshold:
                arr.append(n)
        return arr
