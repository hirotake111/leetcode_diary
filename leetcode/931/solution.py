"""
931. Minimum Falling Path Sum
https://leetcode.com/problems/minimum-falling-path-sum/
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        MAX_VALUE = result = 1000001  # (100 x 100 x 100) + 1
        dp = [[-1] * n for _ in range(n)]

        def dfs(row: int, col: int) -> int:
            """This returns the falling path with a minimum sum"""
            if row == n:  # return 0 so resulting sum includes 0 to row -1
                return 0
            if col < 0 or n <= col:  # If col is out of bound, return MAX_VALUE
                return MAX_VALUE

            # At this time we are sure that 0 <= row < n and 0 < col <= n
            # If we already know the result of dp[row][col], then return it.
            if dp[row][col] != -1:
                return dp[row][col]

            # Else, populate the results of middle, left, and right
            middle = dfs(row + 1, col)
            left = dfs(row + 1, col - 1)
            right = dfs(row + 1, col + 1)
            # Then pick up the minimum one from them, add matrix[row][col]
            dp[row][col] = matrix[row][col] + min(left, middle, right)
            return dp[row][col]

        for i in range(n):
            # Fix row to 0 and iterate over columns
            result = min(result, dfs(0, i))

        return result


class Test(TestCase):
    data_set: List[Tuple[List[List[int]], int]] = [
        ([[2, 1, 3], [6, 5, 4], [7, 8, 9]], 13),
    ]

    def test_solution(self):
        s = Solution()
        for input, expected in self.data_set:
            self.assertEqual(s.minFallingPathSum(input), expected)


if __name__ == "__main__":
    main()
