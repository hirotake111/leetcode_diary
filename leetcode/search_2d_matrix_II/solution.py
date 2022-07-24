from functools import cache
from tkinter import W
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        len_x, len_y = len(matrix[0]), len(matrix)

        @cache
        def dfs(x: int, y: int):
            if x >= len_x or y >= len_y:
                return False

            if matrix[y][x] == target:
                return True

            if matrix[y][x] > target:
                return False

            return dfs(x + 1, y) or dfs(x, y + 1)

        return dfs(0, 0)


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[List[int]], int, bool]] = [
        (
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            5,
            True,
        ),
        (
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            5,
            True,
        ),
        (
            [
                [1, 4, 7, 11, 15],
                [2, 5, 8, 12, 19],
                [3, 6, 9, 16, 22],
                [10, 13, 14, 17, 24],
                [18, 21, 23, 26, 30],
            ],
            20,
            False,
        ),
    ]

    def test_solution(self):
        for matrix, target, expected in self.data:
            self.assertEqual(self.s.searchMatrix(matrix, target), expected)


if __name__ == "__main__":
    main()
