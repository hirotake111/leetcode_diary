from bisect import bisect_left
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # greedy approach
        sub: List[int] = []
        for n in nums:
            if not sub or sub[-1] < n:
                sub.append(n)
            else:
                # find the idex of the smallest number where the number >= x
                idx = bisect_left(sub, n)
                sub[idx] = n
        return len(sub)

        # # dp approach
        # l = len(nums)
        # dp = [1] * l
        # for i in range(l):
        # for j in range(i):
        # if nums[j] < nums[i] and dp[i] <= dp[j]:
        # dp[i] = dp[j] + 1

        # return max(dp)


class Test(TestCase):
    data: List[Tuple[List[int], int]] = [
        ([10, 9, 2, 5, 3, 7, 101, 18], 4),
        ([0, 1, 0, 3, 2, 3], 4),
    ]

    def test_solution(self):
        s = Solution()
        for nums, expected in self.data:
            self.assertEqual(s.lengthOfLIS(nums), expected)


if __name__ == "__main__":
    main()
"""
11,12,13,2,3,20
10,20,30,15,22,25,26,40
10,20,30,15,25,26,40
"""
