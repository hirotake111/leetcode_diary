"""
https://leetcode.com/problems/combination-sum-iii/
216. Combination Sum III
"""
from typing import List, Tuple
from unittest import main, TestCase





class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans: List[List[int]] = []

        # edge case
        if k > sum(range(1, n + 1)) or n > sum(range(9, 9 - k, -1)):
            return []

        def dfs(nums: List[int], x: int):
            nums = nums.copy() + [x]
            s, l = sum(nums), len(nums)

            if l > k or s > n:
                return

            # if l <= k, continue processing
            if s == n:
                if l == k:  # found one possible answer
                    ans.append(nums)
                return
            # now we can say s < n
            # -> recursively call dfs()
            for i in range(x + 1, min(n - s + 1, 10)):
                dfs(nums, i)

        for i in range(1, min(n, 9)):
            dfs([], i)
        return ans


class TestSolution(TestCase):
    s = Solution()
    data: List[Tuple[int, int, List[List[int]]]] = [
        (9, 45, [[1, 2, 3, 4, 5, 6, 7, 8, 9]]),
        (2, 18, []),
        (3, 7, [[1, 2, 4]]),
        (3, 9, [[1, 2, 6], [1, 3, 5], [2, 3, 4]]),
        (4, 1, []),
    ]

    def test_solution(self):
        for k, n, expected in self.data:
            self.assertEqual(self.s.combinationSum3(k, n), expected)


if __name__ == "__main__":
    main()
