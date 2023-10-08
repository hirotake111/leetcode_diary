"""
https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/
1155. Number of Dice Rolls With Target Sum
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        memo = [[-1] * (target + 1) for _ in range(n + 1)]

        if n * k < target:
            return 0

        def dfs(idx: int, rest: int) -> int:
            if rest <= 0:
                return 0

            if memo[idx][rest] != -1:
                return memo[idx][rest]

            if idx == n - 1:
                return 1 if rest <= k else 0

            memo[idx][rest] = sum([dfs(idx + 1, rest - j) for j in range(1, k + 1)])
            return memo[idx][rest]

        return dfs(0, target) % 1000000007


class Test(TestCase):
    data_set: List[Tuple[int, int, int, int]] = [
        (1, 6, 3, 1),
        (2, 6, 7, 6),
        (30, 30, 500, 222616187),
    ]

    def test_solution(self):
        s = Solution()
        for n, k, target, expected in self.data_set:
            self.assertEqual(s.numRollsToTarget(n, k, target), expected)


if __name__ == "__main__":
    main()
