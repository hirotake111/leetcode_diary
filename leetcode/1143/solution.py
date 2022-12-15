"""
1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/
"""
from typing import Dict, List, Tuple
from unittest import TestCase, main


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        This is a classic DP problem
        text1 = "abcde", text2 = "ace"
        1. Since the 1st chars are the same (= "a"), we can break it down to a subproblem.
        -> text1 = "bcde", text2 = "ce" + 1
        2. The next 2 chars aren't the same ("b", "c"), let's divide it into 2 subproblem.
        -> text1 = "cde", text2 = "ce" + 1, or
        -> text1 = "bcde", text2 = "c" + 1
        2-1. The next 2 chars are the same ("c")
        -> text1 = "de", text2 = "e" + 1 + 1
        3. The next 2 chars are not ("d", "e"), so let's divide it in to 2 subproblem.
        -> text1 = "de", text2 = "" + 1 + 1, or
        -> text1 = "e", text2 = "e" + 1 + 1
        3-2. The next 2 chars are the same ("e")
        -> 1 + 1 + 1
        4. With this approach we can start from the last to fist indexes, using DP.
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]  # Need extra column and row

        for i in range(m - 1, -1, -1):  # start from the 2nd last character
            for j in range(n - 1, -1, -1):  # start from the 2nd last character
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1
                else:
                    dp[i][j] = max(dp[i][j + 1], dp[i + 1][j])

        return dp[0][0]


class Test(TestCase):
    data_set: List[Tuple[str, str, int]] = [
        ("abcde", "ace", 3),
        ("abc", "abc", 3),
        ("abc", "def", 0),
    ]

    def test_solution(self):
        for a, b, expected in self.data_set:
            s = Solution()
            self.assertEqual(s.longestCommonSubsequence(a, b), expected)


if __name__ == "__main__":
    main()
