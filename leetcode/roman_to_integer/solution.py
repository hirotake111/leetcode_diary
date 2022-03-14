from unittest import main, TestCase

"""
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
CM: 900
CD: 400
XC: 90
XL: 40
IX: 9
IV: 4
"""


class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0

        # 0
        if len(s) == 0:
            return 0

        # 1000
        while len(s) > 0 and s[0] == "M":
            s = s[1:]
            result += 1000

        # 900
        if len(s) > 1 and s[:2] == "CM":
            s = s[2:]
            result += 900

        # 400
        if len(s) > 1 and s[:2] == "CD":
            s = s[2:]
            result += 400

        # 500
        if len(s) > 0 and s[0] == "D":
            s = s[1:]
            result += 500

        # 100
        while len(s) > 0 and s[0] == "C":
            s = s[1:]
            result += 100

        # 90
        if len(s) > 1 and s[:2] == "XC":
            s = s[2:]
            result += 90

        # 40
        if len(s) > 1 and s[:2] == "XL":
            s = s[2:]
            result += 40

        # 50
        if len(s) > 0 and s[0] == "L":
            s = s[1:]
            result += 50

        # 10
        while len(s) > 0 and s[0] == "X":
            s = s[1:]
            result += 10

        # 9
        if len(s) > 1 and s[:2] == "IX":
            s = s[2:]
            result += 9

        # 4
        if len(s) > 1 and s[:2] == "IV":
            s = s[2:]
            result += 4

        # 5
        if len(s) > 0 and s[0] == "V":
            s = s[1:]
            result += 5

        # 1
        while len(s) > 0 and s[0] == "I":
            s = s[1:]
            result += 1

        return result


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(self.s.romanToInt("III"), 3)
        self.assertEqual(self.s.romanToInt("LVIII"), 58)
        self.assertEqual(self.s.romanToInt("MCMXCIV"), 1994)
        self.assertEqual(self.s.romanToInt("XXVII"), 27)
        self.assertEqual(self.s.romanToInt("XIX"), 19)
        self.assertEqual(self.s.romanToInt("XL"), 40)
        self.assertEqual(self.s.romanToInt("XLIX"), 49)
        self.assertEqual(self.s.romanToInt("L"), 50)
        self.assertEqual(self.s.romanToInt("LI"), 51)
        self.assertEqual(self.s.romanToInt("DCXXI"), 621)
        self.assertEqual(self.s.romanToInt("MMCDXXV"), 2425)
        self.assertEqual(self.s.romanToInt("IX"), 9)
        self.assertEqual(self.s.romanToInt("MDLXX"), 1570)
        self.assertEqual(self.s.romanToInt(""), 0)
        self.assertEqual(self.s.romanToInt("MCM"), 1900)
        self.assertEqual(self.s.romanToInt("MCD"), 1400)
        self.assertEqual(self.s.romanToInt("MD"), 1500)
        self.assertEqual(self.s.romanToInt("MDCCC"), 1800)


if __name__ == "__main__":
    main()
