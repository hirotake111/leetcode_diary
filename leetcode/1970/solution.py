"""
https://leetcode.com/problems/last-day-where-you-can-still-cross/
1970. Last Day Where You Can Still Cross
There is a 1-based binary matrix where 0 represents land and 1 represents water. You are given integers row and col representing the number of rows and columns in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell becomes flooded with water. You are given a 1-based 2D array cells, where cells[i] = [ri, ci] represents that on the ith day, the cell on the r_i_th row and c_i_th column (1-based coordinates) will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to the bottom by only walking on land cells. You can start from any cell in the top row and end at any cell in the bottom row. You can only travel in the four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom by only walking on land cells.
"""
from typing import List, Deque, Tuple
from collections import deque


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def validate(days: int) -> bool:
            cols, seen = set(), set()
            directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
            matrix = [[0] * col for _ in range(row)]
            for i in range(days):
                matrix[cells[i][0] - 1][cells[i][1] - 1] = 1
                cols.add(cells[i][1])
            # Short cut
            if len(cols) < col:
                return True
            # Enqueue cells in the 1st row
            queue: Deque[Tuple[int, int]] = deque()
            for i in range(col):
                if matrix[0][i] == 0:
                    queue.append((0, i))
                    seen.add((0, i))
            # Perform BFS and return true if we reaches the goal (or false otherwise)
            while queue:
                x, y = queue.popleft()
                if x == row - 1:
                    return True
                for a, b in [(c + x, d + y) for (c, d) in directions]:
                    if (
                        0 <= a < row
                        and 0 <= b < col
                        and (a, b) not in seen
                        and matrix[a][b] == 0
                    ):
                        queue.append((a, b))
                        seen.add((a, b))
            return False

        l, r = 1, row * (col - 1)
        answer = 1
        # Binary search the days
        while l <= r:
            mid = (l + r) // 2
            if validate(mid):
                answer = mid
                l = mid + 1
            else:
                r = mid - 1

        return answer
