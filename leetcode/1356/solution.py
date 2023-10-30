"""
https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
1356. Sort Integers by The Number of 1 Bits
"""
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda x: [bin(x).count("1"), x])
        return arr
