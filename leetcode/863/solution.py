"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/description/
863. All Nodes Distance K in Binary Tree

Given the root of a binary tree, the value of a target node target, and an integer k, return an array of the values of all nodes that have a distance k from the target node.

You can return the answer in any order.
"""
from typing import List, Tuple, Dict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        arr: List[int] = []
        parents: Dict[int, TreeNode] = {}

        # Find target node using DFS
        # At the same time, build a hash table for parent nodes
        stack: List[TreeNode] = [root]
        while stack:
            node = stack.pop()
            if node.val == target.val:
                break
            if node.left:
                parents[node.left.val] = node
                stack.append(node.left)
            if node.right:
                parents[node.right.val] = node
                stack.append(node.right)

        # Traverse k times to top and bottom
        seen = set([target.val])
        stack2: List[Tuple[TreeNode, int]] = [(target, k)]
        while stack2:
            node, distance = stack2.pop()
            if distance == 0:
                # Found a node that is a distance k from the target
                arr.append(node.val)
                continue
            parent = parents.get(node.val)
            left, right = node.left, node.right
            if parent and parent.val not in seen:
                # Move to top
                seen.add(parent.val)
                stack2.append((parent, distance - 1))
            if left and left.val not in seen:
                # Move to left
                seen.add(left.val)
                stack2.append((left, distance - 1))
            if right and right.val not in seen:
                # Move to right
                seen.add(right.val)
                stack2.append((right, distance - 1))

        return arr
