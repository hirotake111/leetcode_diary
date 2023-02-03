from collections import defaultdict
from unittest import main, TestCase

"""
01210121012101
PAYPALISHIRING : 14

P   A   H   N
A P L S I I G
Y   I   R
---
01232101232101
PAYPALISHIRING

P     I    N
A   L S  I G
Y A   H R
P     I

P       H
A     S I
Y   I   R
P L     I G
A       N
---
{0: 1, 1: 2, 2: 2, 3: 2, 4: 2, 5: 1})
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


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(self.s.convert("PAYPALISHIRING", 3), "PAHNAPLSIIGYIR")
        self.assertEqual(self.s.convert("PAYPALISHIRING", 4), "PINALSIGYAHRPI")
        self.assertEqual(self.s.convert("PAYPALISHIRING", 400), "PAYPALISHIRING")


if __name__ == "__main__":
    main()
