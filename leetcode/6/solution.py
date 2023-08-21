"""
https://leetcode.com/problems/zigzag-conversion/
6. Zigzag Conversion
"""


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) < numRows:
            return s
        rows = ["" for x in range(len(s))]
        i = 0
        down = False
        for c in s:
            rows[i] += c
            if i == 0 or i == numRows - 1:
                down = not down
            i = i + 1 if down else i - 1

        return "".join(rows)
