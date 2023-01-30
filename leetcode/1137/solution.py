"""
https://leetcode.com/problems/n-th-tribonacci-number/
1137. N-th Tribonacci Number
The Tribonacci sequence Tn is defined as follows: 

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n <= 2:
            return 1
        a, b, c = 0, 1, 1

        for _ in range(n - 2):
            tmp = a + b + c
            a = b
            b = c
            c = tmp
        return c


class Test(TestCase):
    data: List[Tuple[int, int]] = [(4, 4), (25, 1389537)]

    def test_solution(self):
        s = Solution()
        for a, b in self.data:
            self.assertEqual(s.tribonacci(a), b)


if __name__ == "__main__":
    main()
