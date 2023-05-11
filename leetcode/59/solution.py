"""
https://leetcode.com/problems/spiral-matrix-ii/
59. Spiral Matrix II
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
"""
from typing import Tuple, List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[-1] * n for _ in range(n)]
        i, j, END = 1, [0], n**2
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        y, x = 0, -1

        def next_position(y: int, x: int) -> Tuple[int, int]:
            d = j[0]
            a, b = directions[d]
            if (
                y + a < 0
                or n <= y + a
                or x + b < 0
                or n <= x + b
                or matrix[y + a][x + b] != -1
            ):
                # Rotate index for direction
                d = (d + 1) % 4
            a, b = directions[d]
            j[0] = d
            return (y + a, x + b)

        while i <= END:
            y, x = next_position(y, x)
            matrix[y][x] = i
            i += 1

        return matrix
