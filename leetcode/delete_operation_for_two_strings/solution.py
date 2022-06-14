from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # # dynamic programming approach
        l1, l2 = len(word1), len(word2)
        dp: List[List[int]] = [[0] * (l2 + 1) for _ in range(l1 + 1)]
        for i in range(1, l1 + 1):
            for j in range(1, l2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return l1 + l2 - dp[l1][l2] * 2

        # # memoization approach
        # l1, l2 = len(word1), len(word2)
        # memo: List[List[int]] = [[-1] * l2 for _ in range(l1)]

        # def lcs(i: int, j: int):
        #     if i >= l1 or j >= l2:
        #         return 0
        #     if memo[i][j] != -1:
        #         return memo[i][j]
        #     if word1[i] == word2[j]:
        #         memo[i][j] = lcs(i + 1, j + 1) + 1
        #         return memo[i][j]
        #     memo[i][j] = max(lcs(i, j + 1), lcs(i + 1, j))
        #     return memo[i][j]

        # return l1 + l2 - lcs(0, 0) * 2


class Test(TestCase):
    s = Solution()
    data: List[Tuple[str, str, int]] = [
        # ("sea", "eat", 2),
        ("leetcode", "etco", 4),
        ("dinitrophenylhydrazine", "acetylphenylhydrazine", 11),
    ]

    def test_solution(self):
        for word1, word2, expected in self.data:
            self.assertEqual(self.s.minDistance(word1, word2), expected)


if __name__ == "__main__":
    main()
