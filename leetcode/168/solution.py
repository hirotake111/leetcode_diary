"""
https://leetcode.com/problems/excel-sheet-column-title/
168. Excel Sheet Column Title
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        def func(n: int) -> str:
            if n == 0:
                return ""
            quotient, reminder = divmod(n - 1, 26)
            return func(quotient) + chr(reminder + 65)

        return func(columnNumber)
