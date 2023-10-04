"""
https://leetcode.com/problems/combination-sum/
39. Combination Sum
"""
from unittest import main, TestCase
from typing import List

"""
Constraints:
1 <= candidates.length <= 30
1 <= candidates[i] <= 200
All elements of candidates are distinct.
1 <= target <= 500
"""


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        backtrack algorithm approach
        Time: O(n^2)
        Space: O(n)
        """

        def func(comb: List[int], sums: int, idx: int):
            for i in range(idx, l):
                current_sum = sums + candidates[i]
                if current_sum == target:
                    ans.append(comb + [candidates[i]])
                    break
                if current_sum > target:
                    break
                #  less than target
                func(comb + [candidates[i]], current_sum, i)

        ans: List[List[int]] = []
        candidates = list(filter(lambda x: x <= target, sorted(candidates)))
        l = len(candidates)
        func(comb=[], sums=0, idx=0)
        return ans


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[2, 2, 3], [7]]
        self.assertEqual(self.s.combinationSum(candidates, target), expected)
        candidates = [2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        self.assertEqual(self.s.combinationSum(candidates, target), expected)
        candidates = [2, 7, 6, 3, 5, 1]
        target = 9
        expected = [
            [1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 2],
            [1, 1, 1, 1, 1, 1, 3],
            [1, 1, 1, 1, 1, 2, 2],
            [1, 1, 1, 1, 2, 3],
            [1, 1, 1, 1, 5],
            [1, 1, 1, 2, 2, 2],
            [1, 1, 1, 3, 3],
            [1, 1, 1, 6],
            [1, 1, 2, 2, 3],
            [1, 1, 2, 5],
            [1, 1, 7],
            [1, 2, 2, 2, 2],
            [1, 2, 3, 3],
            [1, 2, 6],
            [1, 3, 5],
            [2, 2, 2, 3],
            [2, 2, 5],
            [2, 7],
            [3, 3, 3],
            [3, 6],
        ]
        self.assertEqual(self.s.combinationSum(candidates, target), expected)


if __name__ == "__main__":
    main()
