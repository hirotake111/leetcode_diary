from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        def dfs(node: Optional[TreeNode]) -> str:
            if node is None:
                return ""
            substring = str(node.val)
            left, right = dfs(node.left), dfs(node.right)

            if not (left or right):
                return substring
            substring += f"({left})"
            if right:
                substring += f"({right})"

            return substring

        return dfs(root)
