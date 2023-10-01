"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/
557. Reverse Words in a String III
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join([w[::-1] for w in s.split(" ")])
