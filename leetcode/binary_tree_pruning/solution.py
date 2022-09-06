from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node: Optional[TreeNode]) -> bool:
            if node is None:
                return False

            left = dfs(node.left)
            right = dfs(node.right)

            if not left:
                node.left = None
            if not right:
                node.right = None

            if node.val == 1:
                return True
            # if the result of left or right is true, this node is also nesessary
            return left or right

        if not dfs(root):
            return None
        return root
