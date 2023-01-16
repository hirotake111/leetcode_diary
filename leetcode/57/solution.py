"""
https://leetcode.com/problems/insert-interval/description/
57. Insert Interval

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""
from typing import List
from bisect import bisect


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        def is_overlapped(ax: int, ay: int, bx: int, by: int) -> bool:
            return max(ax, bx) - min(ay, by) <= 0

        # Edge cases
        if intervals == []:
            return [newInterval]
        if intervals[-1][1] < newInterval[0]:
            return intervals + [newInterval]
        if newInterval[1] < intervals[0][0]:
            return [newInterval] + intervals

        position = bisect(intervals, newInterval)
        intervals.insert(position, newInterval)

        answer: List[List[int]] = []
        a = intervals[0]
        for i in range(1, len(intervals)):
            b = intervals[i]
            if is_overlapped(a[0], a[1], b[0], b[1]):
                # Merge two intervals
                a = [min(a[0], b[0]), max(a[1], b[1])]
            else:
                answer.append(a)
                a = b

        answer.append(a)
        return answer


s = Solution()
print(s.insert([[1, 5]], [2, 3]))
