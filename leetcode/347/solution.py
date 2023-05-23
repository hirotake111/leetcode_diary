"""
https://leetcode.com/problems/top-k-frequent-elements/
347. Top K Frequent Elements

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""
from typing import List, Tuple
from collections import Counter
from heapq import heappush, heappop


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Priority queue approach"""
        counter = Counter(nums)
        queue: List[Tuple[int, int]] = []
        answer = []

        # Enqueue n by counts
        for n, counts in counter.items():
            heappush(queue, (-counts, n))

        # Dequeue the number k times from the priority queue
        for _ in range(k):
            _, n = heappop(queue)
            answer.append(n)

        return answer
