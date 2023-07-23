"""
https://leetcode.com/problems/all-possible-full-binary-trees/description/
894. All Possible Full Binary Trees

Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.
"""
from typing import List, Optional, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        if n % 2 == 0:
            return []

        memo: Dict[int, List[Optional[TreeNode]]] = {
            1: [TreeNode()],
            3: [TreeNode(0, TreeNode(), TreeNode())],
        }

        def dfs(n: int) -> List[Optional[TreeNode]]:
            if n in memo:
                return memo[n]

            arr: List[Optional[TreeNode]] = []
            for left in range(1, n, 2):
                right = n - left - 1
                left_arr = dfs(left)
                if left not in memo:
                    memo[left] = left_arr
                right_arr = dfs(right)
                if right not in memo:
                    memo[right] = right_arr
                for j in range(len(left_arr)):
                    for k in range(len(right_arr)):
                        arr.append(TreeNode(0, left_arr[j], right_arr[k]))

            return arr

        return dfs(n)
