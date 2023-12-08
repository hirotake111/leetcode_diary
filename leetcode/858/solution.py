"""
https://leetcode.com/problems/mirror-reflection/
858. Mirror Reflection
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:
        height = 0
        right = True
        while True:
            # move from one to another
            height += q
            right = not right
            if height == p:
                # height is now on the most north
                return 2 if right is True else 1
            if height >= p * 2:
                height -= p * 2
            if height == 0:
                # height is now on the most south
                if right is True:
                    continue
                return 0


class Test(TestCase):
    s = Solution()
    data: List[Tuple[int, int, int]] = [(2, 1, 2), (3, 1, 1)]

    def test_solution(self):
        for p, q, expected in self.data:
            self.assertEqual(self.s.mirrorReflection(p, q), expected)


if __name__ == "__main__":
    main()
