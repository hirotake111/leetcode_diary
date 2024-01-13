"""
https://leetcode.com/problems/range-sum-of-bst/description/?envType=daily-question&envId=2024-01-05
938. Range Sum of BST
"""
from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        queue = deque()
        if root is None:
            return 0
        queue.append(root)
        total = 0
        while len(queue) > 0:
            node = queue.pop()
            if node.val >= low and node.val <= high:
                total += node.val
            if node.left and node.val > low:
                queue.append(node.left)
            if node.right and node.val < high:
                queue.append(node.right)
        return total
