from unittest import main, TestCase

"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        prev = ""
        result = 0
        for c in s:
            if c == "M":
                if prev == "C":
                    result += 900
                else:
                    result += 1000
            if c == "D":
                if prev == "C":
                    # 400
                    result += 400
                else:
                    result += 500
            if c == "C":
                if prev == "C":
                    result += 200
                elif prev == "X":
                    result += 90
                else:
                    result += 100
            if c == "L":
                if prev == "C":
                    result += 100
                if prev == "X":
                    # 40
                    result += 40
                else:
                    result += 50
            if c == "X":
                if prev == "X":
                    result += 20
                elif prev == "I":
                    result += 9
                else:
                    result += 10
            if c == "V":
                if prev == "I":
                    result += 4
                else:
                    result += 5
            if c == "I":
                if prev == "I":
                    result += 1
            prev = c
        if prev == "I":
            result += 1
        return result


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        # self.assertEqual(self.s.romanToInt("III"), 3)
        # self.assertEqual(self.s.romanToInt("LVIII"), 58)
        # self.assertEqual(self.s.romanToInt("MCMXCIV"), 1994)
        # self.assertEqual(self.s.romanToInt("XXVII"), 27)
        # self.assertEqual(self.s.romanToInt("XIX"), 19)
        # self.assertEqual(self.s.romanToInt("XL"), 40)
        # self.assertEqual(self.s.romanToInt("XLIX"), 49)
        # self.assertEqual(self.s.romanToInt("L"), 50)
        # self.assertEqual(self.s.romanToInt("LI"), 51)
        # self.assertEqual(self.s.romanToInt("DCXXI"), 621)
        # self.assertEqual(self.s.romanToInt("MMCDXXV"), 2425)
        # self.assertEqual(self.s.romanToInt("IX"), 9)
        self.assertEqual(self.s.romanToInt("MDLXX"), 1570)


if __name__ == "__main__":
    main()
