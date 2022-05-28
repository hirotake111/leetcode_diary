from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        current = 0
        for i in sorted(nums):
            if i != current:
                return current
            current += 1
        return current


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], int]] = [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ]

    def test_soluiton(self):
        for input, expected in self.data:
            self.assertEqual(self.s.missingNumber(input), expected)


if __name__ == "__main__":
    main()
