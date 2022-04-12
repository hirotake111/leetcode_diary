from typing import List
from unittest import main, TestCase

"""
Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
"""


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        3: previously 0 and will be 1
        4: previously 1 and will be 0
        """
        w = len(board[0])
        h = len(board)

        def func(x: int, y: int):
            count = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    a, b = x + i, y + j
                    if i == j == 0:
                        continue
                    if not (0 <= a < w) or not (0 <= b < h):
                        continue
                    if board[b][a] in (1, 4):
                        count += 1
            if board[y][x] == 1 and (count < 2 or count > 3):
                board[y][x] = 4  # previously 1 and will be 0
            elif board[y][x] == 0 and count == 3:
                board[y][x] = 3  # previously 0 and will be 1

        # update
        for x in range(w):
            for y in range(h):
                func(x, y)

        # update value to either 0 or 1
        for x in range(w):
            for y in range(h):
                board[y][x] = board[y][x] % 2


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        expected = [[0, 0, 0], [1, 0, 1], [0, 1, 1], [0, 1, 0]]
        self.s.gameOfLife(board)
        self.assertEqual(board, expected)
        board = [[1, 1], [1, 0]]
        expected = [[1, 1], [1, 1]]
        self.s.gameOfLife(board)
        self.assertEqual(board, expected)


if __name__ == "__main__":
    main()
