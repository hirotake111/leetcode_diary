"""
https://leetcode.com/problems/gas-station/
134. Gas Station
There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique
"""
from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = -1
        starting_index = -1

        if sum(gas) - sum(cost) < 0:
            return -1
        # Now we are sure that there is at least ONE solution in this pair
        # (And according to the problem description, there is only ONE.)

        for i, diff in enumerate([g - c for g, c in zip(gas, cost)]):
            # If total gas is less than 0 we will seak next index that has a positive diff
            if total_gas < 0:
                if 0 <= diff:
                    # We found the new index that has a positive diff
                    # Update total gas and index
                    total_gas = diff
                    starting_index = i
                continue

            # total gas is positive - add diff to the total
            total_gas += diff

        return starting_index
