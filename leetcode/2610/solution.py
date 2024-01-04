"""
https://leetcode.com/problems/convert-an-array-into-a-2d-array-with-conditions/
2610. Convert an Array Into a 2D Array With Conditions
"""
from typing import List
from collections import Counter


class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        arr = []
        counter = Counter(nums)
        count = sum(counter.values())
        while count > 0:
            sub_arr = []
            for k, v in counter.items():
                if v > 0:
                    sub_arr.append(k)
                    counter[k] -= 1
                    count -= 1
            arr.append(sub_arr)
        return arr
