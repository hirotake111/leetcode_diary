import os
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans = 0
        sign = 1
        # check sign
        if dividend < 0:
            sign = -1
            dividend = abs(dividend)
        if divisor < 0:
            sign *= -1
            divisor = abs(divisor)

        # loop over and increment divisor until dividend < divisor
        tmp_divisor, i = divisor, 1
        while dividend >= divisor:
            if dividend >= tmp_divisor:
                dividend -= tmp_divisor
                ans += i
                i <<= 1
                tmp_divisor <<= 1
            else:
                tmp_divisor = divisor
                i = 1

        return min(max(ans * sign, -2147483648), 2147483647)


class Test(TestCase):
    s = Solution()
    data: List[Tuple[int, int, int]] = [(10, 3, 3), (7, -3, -2), (1, 1, 1)]

    def test_solution(self):
        for dividend, divisor, expected in self.data:
            self.assertEqual(self.s.divide(dividend, divisor), expected)


if __name__ == "__main__":
    main()
