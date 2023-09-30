"""
https://leetcode.com/problems/binary-tree-right-side-view/description/
199. Binary Tree Right Side View
"""
from queue import Queue
from typing import Optional, List, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        values: List[int] = []
        length: int = 0
        queue: Queue[Tuple[TreeNode, int]] = Queue()

        if root is None:
            return []

        queue.put((root, 0))
        while not queue.empty():
            (node, level) = queue.get()
            if level >= length:
                values.append(node.val)
                length += 1
            else:
                values[level] = node.val
            if node.left:
                queue.put((node.left, level + 1))
            if node.right:
                queue.put((node.right, level + 1))

        return values
