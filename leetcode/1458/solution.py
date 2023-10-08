"""
https://leetcode.com/problems/max-dot-product-of-two-subsequences/
1458. Max Dot Product of Two Subsequences
"""
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        dp = [[-1001] * (l2 + 1) for _ in range(l1 + 1)]

        for i in range(l1 - 1, -1, -1):
            for j in range(l2 - 1, -1, -1):
                # dp[i+1][j+1] is the subsequent maximum product you can take
                # So add either dp[i+1][j+1], or 0 (add nothing)
                product = nums1[i] * nums2[j] + max(0, dp[i + 1][j + 1])
                # Compare three products
                dp[i][j] = max(max(product, dp[i][j + 1]), dp[i + 1][j])

        return dp[0][0]
