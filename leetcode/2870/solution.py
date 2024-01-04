"""
https://leetcode.com/problems/minimum-number-of-operations-to-make-array-empty/
2870. Minimum Number of Operations to Make Array Empty
"""
from typing import List
from collections import Counter


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        for n, counts in Counter(nums).items():
            tmp = 0
            while counts > 5:
                counts -= 3
                tmp += 1
            if counts == 5 or counts == 4:
                tmp += 2
            elif counts == 3 or counts == 2:
                tmp += 1
            elif counts == 1:
                return -1
            ops += tmp
        return ops
