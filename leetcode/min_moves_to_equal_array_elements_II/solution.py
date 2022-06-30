from typing import List, Tuple
from unittest import TestCase, main
from statistics import median
from math import trunc


class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        med = trunc(median(nums))
        return sum([abs(med - n) for n in nums])


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], int]] = [
        ([1, 2, 3], 2),
        ([1, 10, 2, 9], 16),
    ]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.minMoves2(input), expected)


if __name__ == "__main__":
    main()

"""
[1,2,3]=2,2,2
1,2,5
    2,2,2 = 4
    3,3,3 = 5
1,1,20
    1,1,1 = 19
    2 = 20
    3 21
    4 22
    5 23
    6 24
    7 25
    8 26
    9 = 27
    11 = 29
    10 = 28
1,2,9
    1 9
    2 8
    3 6
1,2,11
    1 11
    2 10
    3 11
1,2,3,10
    1 12
    2 10
    3 10
    4 12
1,2,4,10
    2 11
    3 11
    4 11
    5 13
1,2,9,10
    4 16
    5 16
    6 16
    7 16
    8 16
    9 16
1,2,9,11
    9 17
    8 17
    7 17
    6 17
1,2,2,9,10
    2 16
    3 17
    4 18
"""
