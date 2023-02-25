"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
121. Best Time to Buy and Sell Stock
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Edge cases
        if len(prices) < 2:
            return 0

        lowest_price = prices[0]
        profit = 0
        for i in range(1, len(prices)):
            current_price = prices[i]
            prev_price = prices[i - 1]
            if prev_price < current_price:
                # It's going up -> update profit
                profit = max(profit, current_price - lowest_price)
            elif current_price < prev_price:
                # It's going down -> update min_value
                lowest_price = min(lowest_price, current_price)

        return profit
