"""
https://leetcode.com/problems/construct-target-array-with-multiple-sums/
1354. Construct Target Array With Multiple Sums
"""
from heapq import heapify, heappop, heappush
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def isPossible(self, target: List[int]) -> bool:
        heap = [-n for n in target]
        heapify(heap)
        summary = sum(target)
        l = len(target)
        expected = [-1] * l

        if l == 0:
            return False

        if l == 1:
            return True if target[0] == 1 else False

        if l == 2:
            large, small = max(target), min(target)
            if large % small == 0 and small != 1:
                return False
            return True

        while True:
            n = -heappop(heap)
            summary -= n
            if n <= summary:
                return False

            n %= summary

            heappush(heap, -n)
            if heap == expected:
                return True
            summary += n


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], bool]] = [
        ([1, 1, 999999999], True),
        ([8, 5], True),
        ([2, 900000002], False),
        ([1, 1000000000], True),
        ([9, 3, 5], True),
        ([1, 1, 1, 2], False),
    ]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.isPossible(input), expected)


if __name__ == "__main__":
    main()
