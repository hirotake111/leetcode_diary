"""
https://leetcode.com/problems/find-duplicate-subtrees/
652. Find Duplicate Subtrees

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.
"""
from typing import List, Optional, DefaultDict
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(
        self, root: Optional[TreeNode]
    ) -> List[Optional[TreeNode]]:
        key_map: DefaultDict[str, List[TreeNode]] = defaultdict(list)

        if root is None:
            return []

        def dfs(node: Optional[TreeNode]):
            if node is None:
                return "None"
            key = f"{node.val}:{dfs(node.left)}:{dfs(node.right)}"
            key_map[key].append(node)
            return key

        dfs(root)
        return [key_map[key][0] for key in key_map.keys() if 1 < len(key_map[key])]
