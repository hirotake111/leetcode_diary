from tkinter import W
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if 30000000 < n:
            # mathmatial approach
            return n > 0 and 1162261467 % n == 0

        if n < 1:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1


class Test(TestCase):
    data: List[Tuple[int, bool]] = [
        (6, False),
        (3**5 + 1, False),
        (3**5 + 9, False),
        (27, True),
        (0, False),
        (9, True),
        (81, True),
        (3, True),
    ]

    def test_solution(self):
        s = Solution()
        for n, expected in self.data:
            self.assertEqual(s.isPowerOfThree(n), expected)


if __name__ == "__main__":
    main()
