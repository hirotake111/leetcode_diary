import enum
from tkinter import N
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        i = 0
        l, current, target = len(nums), sum(nums) - x, 0
        length = 0
        if current == 0:
            return l

        for j, n in enumerate(nums):
            target += n
            if target >= current:
                while target > current and i <= j:
                    target -= nums[i]
                    i += 1
                if target == current:
                    length = max(length, j - i + 1)

        if length == 0:
            return -1
        return l - length


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], int, int]] = [
        (
            [
                8828,
                9581,
                49,
                9818,
                9974,
                9869,
                9991,
                10000,
                10000,
                10000,
                9999,
                9993,
                9904,
                8819,
                1231,
                6309,
            ],
            134365,
            16,
        ),
        ([1, 1, 4, 2, 3], 5, 2),
        ([5, 6, 7, 8, 9], 4, -1),
        ([3, 2, 20, 1, 1, 3], 10, 5),
    ]

    def test_solution(self):
        for nums, x, expected in self.data:
            self.assertEqual(self.s.minOperations(nums, x), expected)


if __name__ == "__main__":
    main()
