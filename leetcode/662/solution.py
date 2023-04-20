"""
https://leetcode.com/problems/maximum-width-of-binary-tree/
662. Maximum Width of Binary Tree

Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes (the leftmost and rightmost non-null nodes), where the null nodes between the end-nodes that would be present in a complete binary tree extending down to that level are also counted into the length calculation.

It is guaranteed that the answer will in the range of a 32-bit signed integer.
"""
from typing import Optional, Deque, Tuple
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue: Deque[Tuple[int, TreeNode]] = deque()
        max_width = 1

        # Edge case
        if root is None:
            return 0

        queue.append((1, root))
        while queue:
            queue_length = len(queue)
            # Pick up all nodes in the queue and push all child nodes in it
            # Index of
            #   left node: idx * 2 -1
            #   right node: idx * 2
            for i in range(queue_length):
                idx, node = queue.popleft()
                if node.left:
                    queue.append((idx * 2 - 1, node.left))
                if node.right:
                    queue.append((idx * 2, node.right))
            # Update the maximum width of the given tree
            if queue:
                max_width = max(max_width, queue[-1][0] - queue[0][0] + 1)

        return max_width
