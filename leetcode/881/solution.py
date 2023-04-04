"""
https://leetcode.com/problems/boats-to-save-people/
881. Boats to Save People

You are given an array people where people[i] is the weight of the ith person, and an infinite number of boats where each boat can carry a maximum weight of limit. Each boat carries at most two people at the same time, provided the sum of the weight of those people is at most limit.

Return the minimum number of boats to carry every given person.
"""
from typing import List


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        l, r = 0, len(people) - 1
        boats = 0

        people.sort()
        while l < r:
            if people[l] + people[r] <= limit:
                # We can carry both l and r with current boat
                l, r = l + 1, r - 1
            else:
                # We can only carry r with current boat
                r -= 1
            # Increment the number of boats
            boats += 1

        # If r == l, we have another person who needs to be carried
        return boats if r < l else boats + 1
