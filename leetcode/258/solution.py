"""
https://leetcode.com/problems/add-digits/
258. Add Digits

Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
"""


class Solution:
    def addDigits(self, num: int) -> int:
        return (num - 1) % 9 + 1
