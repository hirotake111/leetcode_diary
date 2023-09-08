"""
https://leetcode.com/problems/pascals-triangle/
118. Pascal's Triangle
"""
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer: List[List[int]] = [[1], [1, 1]]
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return answer

        prev_arr = answer[1]

        for _ in range(numRows - 2):
            new_arr: List[int] = [1]
            for i in range(len(prev_arr) - 1):
                new_arr.append(prev_arr[i] + prev_arr[i + 1])
            new_arr.append(1)
            answer.append(new_arr)
            prev_arr = new_arr

        return answer


"""
Recursive Solution
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = []

        def func(arr: List[int], i: int):
            new_arr = get_sum_arr(arr) 
            answer.append(new_arr)
            if i > 0:
                func(new_arr, i - 1)
        
        func([], numRows - 1)
        return answer

def get_sum_arr(arr: List[int]) -> List[int]:
    if arr == []:
        return [1]
    if arr == [1]:
        return [1, 1]
    new_arr = [1]
    for i in range(len(arr) - 1):
        new_arr.append(arr[i] + arr[i + 1])
    new_arr.append(1)
    return new_arr
"""
