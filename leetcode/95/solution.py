"""
https://leetcode.com/problems/unique-binary-search-trees-ii/description/
95. Unique Binary Search Trees II
"""
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def create_nodes(begin: int, end: int) -> List[Optional[TreeNode]]:
            if end < begin:
                return [None]
            if begin == end:
                return [TreeNode(begin)]

            nodes: List[Optional[TreeNode]] = []
            for i in range(begin, end + 1):
                left_nodes = create_nodes(begin, i - 1)
                right_nodes = create_nodes(i + 1, end)
                for left in left_nodes:
                    for right in right_nodes:
                        nodes.append(TreeNode(i, left, right))

            return nodes

        return create_nodes(1, n)
