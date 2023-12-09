"""
https://leetcode.com/problems/longest-consecutive-sequence/
128. Longest Consecutive Sequence
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = list(set(nums))
        l = len(s)
        if l < 2:
            return l

        longest = 0
        i = 0
        while i < l - 1:
            current = 1
            while i < l - 1 and s[i + 1] != s[i] + 1:
                i += 1
            while i < l - 1 and s[i + 1] == s[i] + 1:
                current += 1
                i += 1
                if i >= l - 1:
                    break

            longest = max(longest, current)

        return longest


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], int]] = [
        ([1, 2, 0, 1], 3),
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.longestConsecutive(input), expected)


if __name__ == "__main__":
    main()
