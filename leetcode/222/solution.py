from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        # now we are sure we have a root node
        def count_leftmost_level(node: Optional[TreeNode], level: int) -> int:
            if node is None:
                return level
            return count_leftmost_level(node.left, level + 1)

        def count_nodes(n: int, nodes: int) -> int:
            if n == 0:
                return nodes + 1
            return count_nodes(n - 1, nodes + (n - 1) * 2)

        level = count_leftmost_level(root.left, 0)
        left_nodes = count_nodes(level, 0)
        return left_nodes
