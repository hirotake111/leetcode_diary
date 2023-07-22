"""
https://leetcode.com/problems/knight-probability-in-chessboard/description/
688. Knight Probability in Chessboard

On an n x n chessboard, a knight starts at the cell (row, column) and attempts to make exactly k moves. The rows and columns are 0-indexed, so the top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).

A chess knight has eight possible moves it can make, as illustrated below. Each move is two cells in a cardinal direction, then one cell in an orthogonal direction.
"""
from functools import lru_cache


class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        directions = (
            (1, -2),
            (2, -1),
            (2, 1),
            (1, 2),
            (-1, 2),
            (-2, 1),
            (-2, -1),
            (-1, -2),
        )

        @lru_cache(None)
        def dfs(r: int, c: int, k: int) -> int:
            if k == 0:
                return 1

            result = 0
            for row, col in ((a + r, b + c) for a, b in directions):
                if 0 <= row < n and 0 <= col < n:
                    result += dfs(row, col, k - 1)
            return result

        return dfs(row, column, k) / 8**k
