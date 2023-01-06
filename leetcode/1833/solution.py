"""
https://leetcode.com/problems/maximum-ice-cream-bars/
1833. Maximum Ice Cream Bars

It is a sweltering summer day, and a boy wants to buy some ice cream bars.
At the store, there are n ice cream bars. You are given an array costs of length n, where costs[i] is the price of the ith ice cream bar in coins. The boy initially has coins coins to spend, and he wants to buy as many ice cream bars as possible. 
Return the maximum number of ice cream bars the boy can buy with coins coins.
Note: The boy can buy the ice cream bars in any order.
"""
from typing import List


class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        answer = 0
        freq = [0] * (max(costs) + 1)

        # Fill in the list of frequency
        # (each index is cost of icecream)
        for cost in costs:
            freq[cost] += 1

        for cost, amount in enumerate(freq):
            # If frequency is 0, skip it
            if freq[cost] == 0:
                continue
            # If cost * amount is less than coins,
            # simply decrease the coins by cost * amount
            if amount * cost <= coins:
                coins -= amount * cost
                answer += amount
                continue
            # At this point we cannot buy amount * cost
            # So coins // cost should be the amount of icecream we can buy
            answer += coins // cost
            # And don't forget to exist loop
            # (we can't buy icecreams anymore)
            break

        return answer
