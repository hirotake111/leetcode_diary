"""
https://leetcode.com/problems/deepest-leaves-sum/
1302. Deepest Leaves Sum
"""
from typing import Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        if root:
            queue.append(root)

        while queue:
            l = len(queue)
            total = 0
            for _ in range(l):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if len(queue) == 0:
                    return total
