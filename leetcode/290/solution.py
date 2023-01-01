"""
https://leetcode.com/problems/word-pattern/

290. Word Pattern

Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.

Example 1:
Input: pattern = "abba", s = "dog cat cat dog"
Output: true

Example 2:
Input: pattern = "abba", s = "dog cat cat fish"
Output: false

Example 3:
Input: pattern = "aaaa", s = "dog cat cat dog"
Output: false
"""
from typing import Dict


class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        d: Dict[str, str] = {}
        # Split s with spaces
        strs = s.split(" ")

        # Check if two lists have the same num of words and the same unique words
        if len(pattern) != len(strs) or len(set(pattern)) != len(set(strs)):
            return False

        for key, value in zip(pattern, strs):
            value_in_dict = d.get(key, None)
            # If dict doesn't have such a key, insert it.
            if value_in_dict is None:
                d[key] = value
                continue
            # If the value in dict and the value in strs are not the same,
            # return false
            if value_in_dict == value:
                return False

        # We passed all the test -> return true
        return True
