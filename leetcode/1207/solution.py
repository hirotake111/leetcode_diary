"""
1207. Unique Number of Occurrences
https://leetcode.com/problems/unique-number-of-occurrences/
"""
from typing import List, Set
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s: Set[int] = set()

        for value in Counter(arr).values():
            if value in s:
                return False
            s.add(value)

        return True
