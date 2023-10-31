"""
https://leetcode.com/problems/find-the-original-array-of-prefix-xor/
2433. Find the Original Array of Prefix Xor
"""
from typing import List


class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        arr = [pref[0]] * len(pref)
        for i in range(1, len(pref)):
            arr[i] = pref[i] ^ pref[i - 1]
        return arr
