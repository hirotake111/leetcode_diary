"""
https://leetcode.com/problems/maximum-number-of-achievable-transfer-requests/description/
1601. Maximum Number of Achievable Transfer Requests
We have n buildings numbered from 0 to n - 1. Each building has a number of employees. It's transfer season, and some employees want to change the building they reside in.

You are given an array requests where requests[i] = [from_i, to_i] represents an employee's request to transfer from building from_i to building toi.

All buildings are full, so a list of requests is achievable only if for each building, the net change in employee transfers is zero. This means the number of employees leaving is equal to the number of employees moving in. For example if n = 3 and two employees are leaving building 0, one is leaving building 1, and one is leaving building 2, there should be two employees moving to building 0, one employee moving to building 1, and one employee moving to building 2.

Return the maximum number of achievable requests.
"""
from typing import List, Tuple
from functools import lru_cache


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(i: int, balance: Tuple[int]) -> int:
            if i == len(requests):
                return 0 if all(x == 0 for x in balance) else -16
            # copied: the result of processing requests[i]
            # balance: the result of NOT processing requests[i]
            copied = list(balance)
            req = requests[i]
            copied[req[0]] += 1
            copied[req[1]] -= 1
            # As balance involves the success of requests[i],
            # We will add 1 to the result of dfs(i + 1, balance)
            return max(dfs(i + 1, tuple(copied)) + 1, dfs(i + 1, balance))

        return dfs(0, (0,) * n)
