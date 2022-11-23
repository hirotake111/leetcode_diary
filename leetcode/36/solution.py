from typing import List, Set, Tuple
from unittest import TestCase, main


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # validate each row
        for row in range(9):
            s: Set[str] = set()
            for v in board[row]:
                if v == ".":
                    continue
                if v in s:
                    return False
                s.add(v)

        # validate each column
        for col in range(9):
            s = set()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                if board[row][col] in s:
                    return False
                s.add(board[row][col])

        # validate each 3 x 3 sub-box
        for i in (0, 3, 6):
            for j in (0, 3, 6):
                s = set()
                for row in (i, i + 1, i + 2):
                    for col in (j, j + 1, j + 2):
                        if board[row][col] == ".":
                            continue
                        if board[row][col] in s:
                            return False
                        s.add(board[row][col])

        return True


class Test(TestCase):
    data_set: List[Tuple[List[List[str]], bool]] = [
        (
            [
                ["5", "3", ".", ".", "7", ".", ".", ".", "."],
                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                [".", ".", ".", ".", "8", ".", ".", "7", "9"],
            ],
            True,
        ),
    ]

    def test_solution(self):
        s = Solution()
        for input, expected in self.data_set:
            self.assertEqual(s.isValidSudoku(input), expected)


if __name__ == "__main__":
    main()
