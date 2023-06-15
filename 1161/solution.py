"""
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
1161. Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
Return the smallest level x such that the sum of all the values of nodes at level x is maximal.
"""
from typing import Optional, Deque
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        queue: Deque[TreeNode] = deque()
        current_level = min_level = 0
        max_value = -100001

        # Edge case
        if root is None:
            return max_value

        queue.append(root)
        while queue:
            current_level, total = current_level + 1, 0
            for _ in range(len(queue)):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if max_value < total:
                max_value, min_level = total, current_level

        return min_level
