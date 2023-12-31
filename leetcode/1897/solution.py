"""
https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/
1897. Redistribute Characters to Make All Strings Equal
"""
from types import List
from collections import Counter


class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        for v in Counter("".join(words)).values():
            if v % len(words) > 0:
                return False
        return True
