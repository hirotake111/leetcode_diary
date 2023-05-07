"""
https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/description/
1964. Find the Longest Valid Obstacle Course at Each Position

You want to build some obstacle courses. You are given a 0-indexed integer array obstacles of length n, where obstacles[i] describes the height of the ith obstacle.

For every index i between 0 and n - 1 (inclusive), find the length of the longest obstacle course in obstacles such that:

You choose any number of obstacles between 0 and i inclusive.
You must include the ith obstacle in the course.
You must put the chosen obstacles in the same order as they appear in obstacles.
Every obstacle (except the first) is taller than or the same height as the obstacle immediately before it.
Return an array ans of length n, where ans[i] is the length of the longest obstacle course for index i as described above.
"""
from typing import List
import bisect


class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        answer: List[int] = []
        # index + 1: the longest obstacle
        # value: the corresponding lowest value
        # ex: [3] -> [1] -> [1, 5] -> [1, 5, 6] -> [1, 4, 6] -> [1, 2, 6]
        dp: List[int] = []

        for obstacle in obstacles:
            # Get the index i to insert
            i = bisect.bisect_right(dp, obstacle)
            # And i + 1 will be the longest obstacle course in the array
            answer.append(i + 1)
            # If obstacle has the longest value, append a new element
            if i == len(dp):
                dp.append(0)
            dp[i] = obstacle

        return answer
