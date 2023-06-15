"""
https://leetcode.com/problems/kth-largest-sum-in-a-binary-tree/description/
2583. Kth Largest Sum in a Binary Tree

You are given the root of a binary tree and a positive integer k.
The level sum in the tree is the sum of the values of the nodes that are on the same level.
Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.
Note that two nodes are on the same level if they have the same distance from the root.
"""
from typing import Optional, Deque, List
from heapq import heappush, heappop
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        queue: Deque[TreeNode] = deque()
        heap: List[int] = []

        if root is None:
            return -1

        queue.append(root)
        while queue:
            total = 0
            for _ in range(len(queue)):
                node = queue.popleft()
                total += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            heappush(heap, total)
            if k < len(heap):
                heappop(heap)

        return heappop(heap) if len(heap) == k else -1
