from typing import List, Set
from unittest import main, TestCase


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def validate(row: int, col: int, s: Set[int]) -> bool:
            if board[row][col] == ".":
                return True
            if board[row][col] in s:
                return False
            s.add(board[row][col])
            return True

        def validate_row(row: int) -> bool:
            s: Set[int] = set()
            for i in range(9):
                if validate(row, i, s) is False:
                    return False
            return True

        def validate_column(col: int) -> bool:
            s: Set[int] = set()
            for i in range(9):
                if validate(i, col, s) is False:
                    return False
            return True

        def validate_subbox(row: int, col: int) -> bool:
            s: Set[int] = set()
            for i in range(3):
                for j in range(3):
                    if validate(row + i, col + j, s) is False:
                        return False
            return True

        for i in range(9):
            if validate_row(i) is False:
                return False
            if validate_column(i) is False:
                return False
            if i % 3 == 0:
                if (
                    validate_subbox(i, 0)
                    and validate_subbox(i, 3)
                    and validate_subbox(i, 6)
                ) is False:
                    return False

        return True


class TestSolution(TestCase):
    sol = Solution()

    def test_solution(self):
        # [0,0], [0,3], [0,6]
        # [3,0], [3,3], [3,6]
        # [6,0], [6,3], [6,6]
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertEqual(self.sol.isValidSudoku(board), True)
        board = [
            ["8", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "."],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertEqual(self.sol.isValidSudoku(board), False)
        board = [
            ["5", "3", ".", ".", "7", ".", ".", ".", "."],
            ["6", ".", ".", "1", "9", "5", ".", ".", "."],
            [".", "9", "8", ".", ".", ".", ".", "6", "."],
            ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
            ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
            ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
            [".", "6", ".", ".", ".", ".", "2", "8", "7"],
            [".", ".", ".", "4", "1", "9", ".", ".", "5"],
            [".", ".", ".", ".", "8", ".", ".", "7", "9"],
        ]
        self.assertEqual(self.sol.isValidSudoku(board), False)


if __name__ == "__main__":
    main()
