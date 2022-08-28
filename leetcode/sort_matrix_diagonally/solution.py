from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        rows, colums = len(mat), len(mat[0])
        arr: List[int] = []

        def fetch(i: int, j: int, arr: List[int]) -> List[int]:
            if rows <= i or colums <= j:
                return arr
            return fetch(i + 1, j + 1, arr + [mat[i][j]])

        def replace(i: int, j: int, k: int, arr: List[int]) -> None:
            if rows <= i or colums <= j:
                return
            mat[i][j] = arr[k]
            replace(i + 1, j + 1, k + 1, arr)

        for i in range(rows):
            j = 0
            arr = fetch(i, j, [])
            replace(i, j, 0, sorted(arr))

        for j in range(colums):
            i = 0
            arr = fetch(i, j, [])
            replace(i, j, 0, sorted(arr))

        return mat


class Test(TestCase):
    data: List[Tuple[List[List[int]], List[List[int]]]] = [
        (
            [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]],
            [[1, 1, 1, 1], [1, 2, 2, 2], [1, 2, 3, 3]],
        ),
        (
            [
                [11, 25, 66, 1, 69, 7],
                [23, 55, 17, 45, 15, 52],
                [75, 31, 36, 44, 58, 8],
                [22, 27, 33, 25, 68, 4],
                [84, 28, 14, 11, 5, 50],
            ],
            [
                [5, 17, 4, 1, 52, 7],
                [11, 11, 25, 45, 8, 69],
                [14, 23, 25, 44, 58, 15],
                [22, 27, 31, 36, 50, 66],
                [84, 28, 75, 33, 55, 68],
            ],
        ),
    ]

    def test_solution(self):
        s = Solution()
        for input, expected in self.data:
            self.assertEqual(s.diagonalSort(input), expected)


if __name__ == "__main__":
    main()
