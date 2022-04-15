from typing import List
from unittest import main, TestCase


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        # generate n x n matrix filled with 0
        mtx = [[0] * n for x in range(n)]
        i, di = 0, -1
        x, y = -1, 0
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        while i < n * n:
            di += 1
            d = directions[di % 4]
            while True:
                # move to the next position
                i += 1
                x += d[0]
                y += d[1]
                # set value
                mtx[y][x] = i
                # check if the next direction is valid
                if (
                    not (0 <= y + d[1] < n)
                    or not (0 <= x + d[0] < n)
                    or mtx[y + d[1]][x + d[0]] != 0
                ):
                    # change direction
                    break

        return mtx


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        expected = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
        self.assertEqual(self.s.generateMatrix(3), expected)
        expected = [[1]]
        self.assertEqual(self.s.generateMatrix(1), expected)


if __name__ == "__main__":
    main()
