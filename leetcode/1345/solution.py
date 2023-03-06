"""
https://leetcode.com/problems/jump-game-iv/
1345. Jump Game IV
Given an array of integers arr, you are initially positioned at the first index of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.
"""
from typing import List, Deque, DefaultDict, Tuple
from collections import deque, defaultdict
from unittest import TestCase, main


class Solution:
    def minJumps(self, arr: List[int]) -> int:
        # Edge case
        if len(arr) == 1:
            return 0

        steps = 0
        visited = [True] + [False] * (len(arr) - 1)
        q: Deque[int] = deque()
        q.append(0)
        hm: DefaultDict[int, List[int]] = defaultdict(list)

        # Create hash map
        for i in range(len(arr)):
            hm[arr[i]].append(i)

        while q:
            for _ in range(len(q)):
                i = q.popleft()

                # If i is the last index, return steps
                if i == len(arr) - 1:
                    return steps

                # Search i - 1
                if 0 <= i - 1 and not visited[i - 1]:
                    visited[i - 1] = True
                    q.append(i - 1)

                # Search i + 1
                if i + 1 < len(arr) and not visited[i + 1]:
                    visited[i + 1] = True
                    q.append(i + 1)

                # Search hm[arr[i]]
                while hm[arr[i]]:
                    j = hm[arr[i]].pop()
                    if not visited[j]:
                        visited[j] = True
                        q.append(j)

            steps += 1

        raise ValueError("Could't find the answer")


class Test(TestCase):
    cases: List[Tuple[List[int], int]] = [
        ([7, 7, 2, 1, 7, 7, 7, 3, 4, 1], 3),
    ]

    def test_solution(self):
        solution = Solution()
        for arr, expected in self.cases:
            self.assertEqual(solution.minJumps(arr), expected)


if __name__ == "__main__":
    main()
