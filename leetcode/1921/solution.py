"""
https://leetcode.com/problems/eliminate-maximum-number-of-monsters/
1921. Eliminate Maximum Number of Monsters
"""

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        arr = [d // s + (1 if d % s else 0) for d, s in zip(dist, speed)]
        arr.sort()
        for mins_taken, mins_to_reach in enumerate(arr):
            if mins_taken >= mins_to_reach:
                return mins_taken
        return len(dist)
