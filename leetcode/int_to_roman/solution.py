from unittest import main, TestCase


"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
---
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""

        tmp = num % 10
        num -= tmp
        if tmp == 9:
            result = "IX"
        elif tmp == 4:
            result = "IV"
        else:
            if tmp >= 5:
                result = "V"
                tmp -= 5
            while tmp > 0:
                result += "I"
                tmp -= 1

        tmp = num % 100
        num -= tmp
        if tmp == 90:
            result = "XC" + result
        elif tmp == 40:
            result = "XL" + result
        else:
            w = ""
            if tmp >= 50:
                w = "L"
                tmp -= 50
            while tmp > 0:
                w += "X"
                tmp -= 10
            result = w + result

        tmp = num % 1000
        num -= tmp
        if tmp == 900:
            result = "CM" + result
        elif tmp == 400:
            result = "CD" + result
        else:
            w = ""
            if tmp >= 500:
                w += "D"
                tmp -= 500
            while tmp > 0:
                w += "C"
                tmp -= 100
            result = w + result

        while num > 0:
            result = "M" + result
            num -= 1000

        return result


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(self.s.intToRoman(3), "III")
        self.assertEqual(self.s.intToRoman(9), "IX")
        self.assertEqual(self.s.intToRoman(4), "IV")
        self.assertEqual(self.s.intToRoman(8), "VIII")
        self.assertEqual(self.s.intToRoman(58), "LVIII")
        self.assertEqual(self.s.intToRoman(1994), "MCMXCIV")
        self.assertEqual(self.s.intToRoman(4444), "MMMMCDXLIV")
        self.assertEqual(self.s.intToRoman(3999), "MMMCMXCIX")


if __name__ == "__main__":
    main()
