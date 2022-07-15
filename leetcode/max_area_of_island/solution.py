from tkinter import W
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        len_row, len_col = len(grid), len(grid[0])
        answer = 0

        def dfs(row: int, col: int) -> int:
            summary = 1
            grid[row][col] = 2  # set it as visited
            if row > 0 and grid[row - 1][col] == 1:
                summary += dfs(row - 1, col)
            if col < len_col - 1 and grid[row][col + 1] == 1:
                summary += dfs(row, col + 1)
            if row < len_row - 1 and grid[row + 1][col] == 1:
                summary += dfs(row + 1, col)
            if col > 0 and grid[row][col - 1] == 1:
                summary += dfs(row, col - 1)

            return summary

        for i in range(len_row):
            for j in range(len_col):
                if grid[i][j] == 1:
                    answer = max(answer, dfs(i, j))

        return answer


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[List[int]], int]] = [
        (
            [
                [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            ],
            6,
        ),
        ([[0, 0, 0, 0, 0, 0, 0, 0]], 0),
    ]

    def test_solution(self):
        for input, expecetd in self.data:
            self.assertEqual(self.s.maxAreaOfIsland(input), expecetd)


if __name__ == "__main__":
    main()
