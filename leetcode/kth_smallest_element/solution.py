from typing import List, Tuple
from unittest import TestCase, main
from itertools import chain


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        return sorted(list(chain.from_iterable(matrix)))[k - 1]


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[List[int]], int, int]] = [
        ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8, 13),
        ([[-5]], 1, -5),
    ]

    def test_solution(self):
        for matrix, k, expected in self.data:
            self.assertEqual(self.s.kthSmallest(matrix, k), expected)


if __name__ == "__main__":
    main()
