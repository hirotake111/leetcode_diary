from typing import List, Optional, Tuple
from unittest import TestCase, main


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans: List[List[int]] = []
        nums = sorted(nums)

        def backtrack(candidate: List[int], result: List[int]):
            prev: int = -11
            if not candidate:
                ans.append(result)
                return

            for i, n in enumerate(candidate):
                if prev == n:
                    continue
                prev = n
                backtrack(candidate[:i] + candidate[i + 1 :], result + [n])

        backtrack(nums, [])
        return ans


class TestSolution(TestCase):
    s = Solution()
    data: List[Tuple[List[int], List[List[int]]]] = [
        ([1, 1, 2], [[1, 1, 2], [1, 2, 1], [2, 1, 1]]),
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.permuteUnique(input), expected)


if __name__ == "__main__":
    main()
