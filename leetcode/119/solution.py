"""
https://leetcode.com/problems/pascals-triangle-ii/
119. Pascal's Triangle II
"""
from typing import List


class Solution:
    def getRow(self, i: int) -> List[int]:
        if i == 0:
            return [1]

        arr = [1, 1]
        while i > 1:
            for j in range(len(arr) - 1):
                arr[j] += arr[j + 1]
            arr = [1] + arr[:-1] + [1]
            i -= 1

        return arr
