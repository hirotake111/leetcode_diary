"""
https://leetcode.com/problems/multiply-strings/
43. Multiply Strings
"""
zero = ord("0")


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(convert(num1) * convert(num2))


def convert(num: str) -> int:
    return sum([(ord(n) - zero) * 10**i for i, n in enumerate(num[::-1])])
