from typing import Optional, Set


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    total: int = 0
    cameras: Set[TreeNode] = set()

    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        def dfs(node: Optional[TreeNode], parent: Optional[TreeNode]):
            if node is None:
                return

            dfs(node.left, node)
            dfs(node.right, node)

            if (
                node.left is None
                and node.right is None
                and parent
                and parent not in self.cameras
            ):
                self.cameras.add(parent)
                self.total += 1
                return

            if (
                node.left not in self.cameras
                or node.right not in self.cameras
                and node
                and node not in self.cameras
            ):
                self.cameras.add(node)
                self.total += 1
                return

        if root is None:
            return 0

        dfs(root.left, root)
        dfs(root.right, root)
        return self.total
