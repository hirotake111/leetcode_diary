"""
https://leetcode.com/problems/coin-change/
322. Coin Change
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """bottom up approach"""
        dp: List[int] = [0] + [amount + 1] * amount

        for a in range(1, amount + 1):  # 1...amount
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - coin])  # 1 is "coin" itself
        return dp[amount] if dp[amount] != amount + 1 else -1


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], int, int]] = [
        ([1, 2, 5], 11, 3),
        ([186, 419, 83, 408], 6249, 20),
        ([2], 3, -1),
        ([1], 0, 0),
    ]

    def test_solution(self):
        for coins, amount, expected in self.data:
            self.assertEqual(self.s.coinChange(coins, amount), expected)


if __name__ == "__main__":
    main()
