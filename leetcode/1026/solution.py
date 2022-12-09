"""
1026. Maximum Difference Between Node and Ancestor
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], low: int, high: int, answer: int) -> int:
            if node is None:
                return answer
            # Calculate the highest number among values
            v1 = abs(low - node.val)
            v2 = abs(high - node.val)
            answer = max([answer, v1, v2])

            # Determine the lowest and the highest node values
            low = min(low, node.val)
            high = max(high, node.val)

            # go to the next nodes
            result1 = dfs(node.left, low, high, answer)
            result2 = dfs(node.right, low, high, answer)
            return max(result1, result2)

        if root is None:
            return 0
        return dfs(root, root.val, root.val, 0)
