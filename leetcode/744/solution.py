"""
https://leetcode.com/problems/find-smallest-letter-greater-than-target/description/
744. Find Smallest Letter Greater Than Target
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.
"""
from typing import List
import bisect


class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # filtered = list(filter(lambda x : target < x, letters))
        # if len(filtered) == 0:
        #    return letters[0]
        # return filtered[0]

        idx = bisect.bisect_right(letters, target)
        if idx == len(letters):
            return letters[0]
        return letters[idx]
