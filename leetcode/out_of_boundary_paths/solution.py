from queue import Queue
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def findPaths(
        self, m: int, n: int, maxMove: int, startRow: int, startColumn: int
    ) -> int:
        # recursion with meoition
        memo = [[[-1] * (maxMove + 1) for _ in range(n + 1)] for _ in range(m + 1)]

        def dfs(row: int, col: int, remain: int) -> int:
            if remain < 0:
                return 0
            if row < 0 or row >= m or col < 0 or col >= n:
                return 1

            if memo[row][col][remain] >= 0:
                return memo[row][col][remain]

            a = dfs(row - 1, col, remain - 1)
            b = dfs(row + 1, col, remain - 1)
            c = dfs(row, col - 1, remain - 1)
            d = dfs(row, col + 1, remain - 1)

            memo[row][col][remain] = a + b + c + d
            return memo[row][col][remain]

        return dfs(startRow, startColumn, maxMove) % 100000000007

        # # brute force approach
        # if startRow == -1 or startColumn == -1 or startRow == m or startColumn == n:
        # return 1
        # if maxMove == 0:
        # return 0
        # return (
        # self.findPaths(m, n, maxMove - 1, startRow - 1, startColumn)
        # + self.findPaths(m, n, maxMove - 1, startRow + 1, startColumn)
        # + self.findPaths(m, n, maxMove - 1, startRow, startColumn - 1)
        # + self.findPaths(m, n, maxMove - 1, startRow, startColumn + 1)
        # )


class Test(TestCase):
    s = Solution()
    data: List[Tuple[int, int, int, int, int, int]] = [
        (8, 6, 10, 4, 3, 72337),
        (3, 3, 3, 1, 0, 13),
        (2, 2, 2, 0, 0, 6),
        (1, 3, 3, 0, 1, 12),
    ]

    def test_solution(self):
        for m, n, maxMove, startRow, startColumn, expected in self.data:
            self.assertEqual(
                self.s.findPaths(m, n, maxMove, startRow, startColumn), expected
            )


if __name__ == "__main__":
    main()
