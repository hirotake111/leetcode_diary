"""
https://leetcode.com/problems/pacific-atlantic-water-flow/
417. Pacific Atlantic Water Flow
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, columns = len(heights), len(heights[0])
        directions: List[Tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        p_matrix = [[0] * columns for _ in range(rows)]
        a_matrix = [[0] * columns for _ in range(rows)]
        answer: List[List[int]] = []

        def dfs(
            row: int,
            col: int,
            edge_row: int,
            edge_col: int,
            matrix: List[List[int]],
        ) -> List[List[int]]:
            matrix[row][col] = 1
            for direction in directions:
                next_row, next_col = row + direction[0], col + direction[1]
                if not (0 <= next_row < rows and 0 <= next_col < columns):
                    continue
                if (
                    heights[row][col] <= heights[next_row][next_col]
                    or next_row == edge_row
                    or next_col == edge_col
                ) and matrix[next_row][next_col] == 0:
                    matrix = dfs(next_row, next_col, edge_row, edge_col, matrix)

            return matrix

        p_matrix = dfs(0, 0, 0, 0, p_matrix)
        a_matrix = dfs(rows - 1, columns - 1, rows - 1, columns - 1, a_matrix)

        for i in range(rows):
            for j in range(columns):
                if p_matrix[i][j] == 1 and a_matrix[i][j] == 1:
                    answer.append([i, j])

        return answer


class Test(TestCase):
    data: List[Tuple[List[List[int]], List[List[int]]]] = [
        # (
        # [[10, 10, 10], [10, 1, 10], [10, 10, 10]],
        # [[0, 0], [0, 1], [0, 2], [1, 0], [1, 2], [2, 0], [2, 1], [2, 2]],
        # ),
        (
            [
                [1, 2, 2, 3, 5],
                [3, 2, 3, 4, 4],
                [2, 4, 5, 3, 1],
                [6, 7, 1, 4, 5],
                [5, 1, 1, 2, 4],
            ],
            [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]],
        ),
        ([[1]], [[0, 0]]),
    ]

    def test_solution(self):
        s = Solution()
        for given, expected in self.data:
            self.assertEqual(s.pacificAtlantic(given), expected)


if __name__ == "__main__":
    main()
