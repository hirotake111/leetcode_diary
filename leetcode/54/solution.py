"""
https://leetcode.com/problems/spiral-matrix/
54. Spiral Matrix
Given an m x n matrix, return all elements of the matrix in spiral order.
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
        answer = [-101] * (m * n)
        i, j = -1, 0  # i: index of directions, j: index of answer
        x, y = 0, -1

        def inside(x: int, y: int, nx: int, ny: int) -> bool:
            """Returns True if"""
            a, b = x + nx, y + ny
            return (
                answer[-1] == -101
                and 0 <= a < m
                and 0 <= b < n
                and matrix[a][b] != -101
            )

        while answer[-1] == -101:
            # Update direction
            i = (i + 1) % 4
            next_x, next_y = directions[i]
            while (
                answer[-1] == -101
                and 0 <= x + next_x < m
                and 0 <= y + next_y < n
                and matrix[x + next_x][y + next_y] != -101
            ):
                x, y = x + next_x, y + next_y
                answer[j] = matrix[x][y]
                matrix[x][y] = -101
                j += 1

        return answer
