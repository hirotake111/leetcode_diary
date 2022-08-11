from re import I
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(
        self,
        val=0,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node: Optional[TreeNode], low: int, high: int):
            if node is None:
                return True

            if node.val <= low or high <= node.val:
                return False

            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)

        return dfs(root, -2147483649, 2147483648)
