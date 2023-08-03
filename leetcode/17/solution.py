"""
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List

digits_map = {
    "2": "abc",
    "3": "def",
    "4": "ghi",
    "5": "jkl",
    "6": "mno",
    "7": "pqrs",
    "8": "tuv",
    "9": "wxyz",
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return list(digits_map[digits])

        return [
            ch + sub_ch
            for sub_ch in self.letterCombinations(digits[1:])
            for ch in digits_map[digits[0]]
        ]
