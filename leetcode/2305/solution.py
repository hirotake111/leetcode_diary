"""
https://leetcode.com/problems/fair-distribution-of-cookies/
2305. Fair Distribution of Cookies
You are given an integer array cookies, where cookies[i] denotes the number of cookies in the ith bag. You are also given an integer k that denotes the number of children to distribute all the bags of cookies to. All the cookies in the same bag must go to the same child and cannot be split up.

The unfairness of a distribution is defined as the maximum total cookies obtained by a single child in the distribution.

Return the minimum unfairness of all distributions.
"""
from typing import List


class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        answer = float("inf")
        fair = [0] * k

        def rec(i):
            nonlocal answer, fair
            if i == len(cookies):
                answer = min(answer, max(fair))
                return
            if answer <= max(fair):
                return
            for j in range(k):
                fair[j] += cookies[i]
                rec(i + 1)
                fair[j] -= cookies[i]

        rec(0)
        return int(answer)
