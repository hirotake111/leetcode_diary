"""
https://leetcode.com/problems/k-th-symbol-in-grammar/
779. K-th Symbol in Grammar

We can see the problem as binary tree structure.
Therefore binary search works to solve it.
"""


class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1:
            return 0
        if k % 2 == 0:
            return 1 - self.kthGrammar(n - 1, k // 2)
        return self.kthGrammar(n - 1, (k + 1) // 2)
