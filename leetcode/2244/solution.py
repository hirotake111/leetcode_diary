"""
https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
2244. Minimum Rounds to Complete All Tasks

You are given a 0-indexed integer array tasks, where tasks[i] represents the difficulty level of a task. In each round, you can complete either 2 or 3 tasks of the same difficulty level.

Return the minimum rounds required to complete all the tasks, or -1 if it is not possible to complete all the tasks.
"""
from typing import List
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        answer = 0

        for counts in Counter(tasks).values():
            if counts == 1:
                return -1

            if counts == 2:
                answer += 1
                continue

            quotient, reminder = divmod(counts, 3)
            if reminder == 0:
                answer += quotient
            else:
                answer += quotient + 1

        return answer
