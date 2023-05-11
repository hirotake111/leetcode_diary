"""
https://leetcode.com/problems/uncrossed-lines/submissions/
1035. Uncrossed Lines
You are given two integer arrays nums1 and nums2. We write the integers of nums1 and nums2 (in the order they are given) on two separate horizontal lines.

We may draw connecting lines: a straight line connecting two numbers nums1[i] and nums2[j] such that:

nums1[i] == nums2[j], and
the line we draw does not intersect any other connecting (non-horizontal) line.
Note that a connecting line cannot intersect even at the endpoints (i.e., each number can only belong to one connecting line).

Return the maximum number of connecting lines we can draw in this way.
"""
from typing import List


class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        """DP approach"""
        m, n = len(nums1), len(nums2)
        prev = [0] * (n + 1)

        for i in range(m):
            dp = [0] * (n + 1)
            for j in range(n):
                if nums1[i] == nums2[j]:
                    dp[j + 1] = 1 + prev[j]
                else:
                    dp[j + 1] = max(dp[j], prev[j + 1])
            prev = dp
        return prev[-1]

        """Recursive Approach"""
        # dp: Dict[Tuple[int, int]] = {}
        # def dfs(i: int, j: int) -> int:
        #    if i == len(nums1) or j == len(nums2):
        #        return 0
        #    if (i, j) in dp:
        #        return dp[(i, j)]
        #
        #    if nums1[i] == nums2[j]:
        #        dp[(i, j)] = 1 + dfs(i + 1, j + 1)
        #    else:
        #        dp[(i, j)] = max(dfs(i, j + 1), dfs(i + 1, j))
        #    return dp[(i, j)]

        # return dfs(0, 0)
