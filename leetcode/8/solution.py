"""
https://leetcode.com/problems/string-to-integer-atoi/
8. String to Integer (atoi)
"""
from unittest import main, TestCase


class Solution:
    def myAtoi(self, s: str) -> int:
        result = ""
        n = 1
        s = s.strip()

        if s == "":
            return 0
        if s[0] in "-+":
            if s[0] == "-":
                n = -1
            s = s[1:]

        for c in s:
            if c not in "1234567890":
                break
            result += c
        if result == "":
            return 0
        result = int(result) * n
        if result < -(2**31):
            return -(2**31)
        if result > 2**31 - 1:
            return 2**31 - 1
        return result


class TestSolution(TestCase):
    def test_solution(self):
        s = Solution()
        self.assertEqual(s.myAtoi("123"), 123)
        self.assertEqual(s.myAtoi("0032"), 32)
        self.assertEqual(s.myAtoi("-123"), -123)
        self.assertEqual(s.myAtoi("-+12"), 0)
        self.assertEqual(s.myAtoi("number is 12"), 0)
        self.assertEqual(s.myAtoi("   +0 123"), 0)


if __name__ == "__main__":
    main()
