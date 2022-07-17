from itertools import combinations
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        l = len(candidates)
        filtered: List[int] = []
        combinations: List[List[int]] = []
        for candidate in candidates:
            if candidate == target:
                combinations.append([candidate])
            elif candidate < target:
                filtered.append(candidate)

        filtered.sort()

        for i in range(l):
            sub_candidates: List[List[int]] = []


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
