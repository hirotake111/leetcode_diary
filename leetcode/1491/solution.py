"""
https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/

1491. Average Salary Excluding the Minimum and Maximum Salary

You are given an array of unique integers salary where salary[i] is the salary of the ith employee.
Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.
"""
from typing import List


class Solution:
    def average(self, salary: List[int]) -> float:
        max_value, min_value = 1000, 1000000
        total, n = 0, -2
        for s in salary:
            total += s
            n += 1
            max_value = max(max_value, s)
            min_value = min(min_value, s)
        return (total - max_value - min_value) / n
