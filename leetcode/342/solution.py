from typing import List, Tuple
from unittest import TestCase, main


"""
https://leetcode.com/problems/power-of-four/
342. Power of Four
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        if n == 1 or n == 4:
            return True
        quotient, reminder = divmod(n, 4)
        if reminder != 0:
            return False
        return self.isPowerOfFour(quotient)
