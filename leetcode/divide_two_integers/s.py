from unittest import main, TestCase

"""
Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [-231, 231 -1]. 
For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.
"""


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        sign = 1 if (dividend > 0) == (divisor > 0) else -1
        dividend, divisor = abs(dividend), abs(divisor)
        ans = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                ans += i
                i <<= 1
                temp <<= 1
        if sign < 0:
            ans = -ans
        return max(min(ans, 2147483647), -2147483648)


class TestSolution(TestCase):
    s = Solution()

    def test_s(self):
        self.assertEqual(self.s.divide(dividend=10, divisor=3), 3)
        self.assertEqual(self.s.divide(dividend=7, divisor=-3), -2)
        self.assertEqual(self.s.divide(dividend=1, divisor=1), 1)
        self.assertEqual(self.s.divide(-2147483648, -1), 2147483647)
        self.assertEqual(self.s.divide(2147483647, 2), 1073741823)


if __name__ == "__main__":
    main()
