"""
https://leetcode.com/problems/number-of-flowers-in-full-bloom/
2251. Number of Flowers in Full Bloom
"""
from typing import List
from heapq import heappush, heappop


class Solution:
    def fullBloomFlowers(
        self, flowers: List[List[int]], people: List[int]
    ) -> List[int]:
        starts, ends, answer = [], [], [0] * len(people)

        # Create heap queue of start and end respectively
        for start, end in flowers:
            heappush(starts, start)
            heappush(ends, end)

        blooms = done = 0
        # sort people while preserving original index
        for i, p in sorted(enumerate(people), key=lambda x: x[1]):
            # count up blooms and pop up item from starts until starts > p
            while starts and starts[0] <= p:
                heappop(starts)
                blooms += 1

            # count up done and pop up item from ends until ends >= p
            while ends and ends[0] < p:
                heappop(ends)
                done += 1

            answer[i] = blooms - done

        return answer
