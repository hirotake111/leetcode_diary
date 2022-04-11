from typing import List
from unittest import main, TestCase


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        a, y = divmod(k, len(grid[0]))
        x = a % len(grid)

        # shift rows x times
        if x > 0:
            grid = grid[-x:] + grid[:-x]

        if y == 0:
            return grid

        # shift columns y times
        carry = grid[-1][-y:]
        for i in range(len(grid)):
            tmp = grid[i][-y:].copy()
            grid[i] = carry + grid[i][:-y]
            carry = tmp

        return grid


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        k = 1
        expected = [[9, 1, 2], [3, 4, 5], [6, 7, 8]]
        # 4 >  [6,7,8],[9,1,2][3,4,5]
        self.assertEqual(self.s.shiftGrid(grid, k), expected)
        grid = [[3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10], [12, 0, 21, 13]]
        k = 4
        expected = [[12, 0, 21, 13], [3, 8, 1, 9], [19, 7, 2, 5], [4, 6, 11, 10]]
        self.assertEqual(self.s.shiftGrid(grid, k), expected)
        grid = [[1], [2], [3], [4], [7], [6], [5]]
        k = 23
        # output = [[4], [7], [6], [5], [1], [2], [3]]
        expected = [[6], [5], [1], [2], [3], [4], [7]]
        self.assertEqual(self.s.shiftGrid(grid, k), expected)


if __name__ == "__main__":
    main()
