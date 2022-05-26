from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n > 0:
            d, m = divmod(n, 2)
            ans += m
            n = d
        return ans
