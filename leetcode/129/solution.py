"""
https://leetcode.com/problems/sum-root-to-leaf-numbers/
129. Sum Root to Leaf Numbers
You are given the root of a binary tree containing digits from 0 to 9 only.

Each root-to-leaf path in the tree represents a number.

For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.

A leaf node is a node with no children.
"""
from collections import deque
from typing import Optional, Deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Edge case
        if root is None:
            return 0

        answer = 0
        q: Deque[TreeNode] = deque()
        q.append(root)
        while q:
            node = q.popleft()
            if node.left is None and node.right is None:
                # node is a leaf -> add the value to the answer
                answer += node.val
                continue

            if node.left:
                # Add node.val * 10 to the chid node
                node.left.val += node.val * 10
                # Push it to the queue
                q.append(node.left)

            # And the same thing can be applied to the right node
            if node.right:
                node.right.val += node.val * 10
                q.append(node.right)

        return answer
