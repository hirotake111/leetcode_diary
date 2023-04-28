"""
https://leetcode.com/problems/bulb-switcher/

319. Bulb Switcher

There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.
"""
from math import sqrt


class Solution:
    def bulbSwitch(self, n: int) -> int:
        # A bulb is ON only if the root of the round is integer
        return int(sqrt(n))
