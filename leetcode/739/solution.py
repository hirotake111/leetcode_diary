"""
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures/
"""
from typing import List
from unittest import TestCase, main


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack: List[int] = []
        # List of indexes, not temperatures
        answer = [0 for _ in range(len(temperatures))]

        # Pick up index and temperature from temperatures one by one
        for idx, temparature in enumerate(temperatures):
            # Loop while the stack has an item and the current temperature is
            # greater than the peak in the stack.
            while len(stack) != 0 and temperatures[stack[-1]] < temparature:
                peak_idx = stack.pop()
                # idx - peak_idx will be the num of days you have to wait to get a warmer temperature.
                answer[peak_idx] = idx - peak_idx
            # Now the stack is empty or the peak in the stack is less than or equal to the current one,
            # just push it to the stack
            stack.append(idx)

        return answer
