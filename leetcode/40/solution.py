"""
https://leetcode.com/problems/combination-sum-ii/
40. Combination Sum II
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        n = len(candidates)
        candidates.sort()

        def dfs(target: int, idx: int, path):
            if target <= 0:
                if target == 0:
                    answer.append(path)
                return

            for i in range(idx, n):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                dfs(target - candidates[i], i + 1, path + [candidates[i]])

        dfs(target, 0, [])
        return answer


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], int, List[List[int]]]] = [
        ([10, 1, 2, 7, 6, 1, 5], 8, [[1, 1, 6], [1, 2, 5], [1, 7], [2, 6]]),
        ([2, 5, 2, 1, 2], 5, [[1, 2, 2], [5]]),
    ]

    def test_solution(self):
        for candidates, target, expected in self.data:
            self.assertEqual(self.s.combinationSum2(candidates, target), expected)


if __name__ == "__main__":
    main()
