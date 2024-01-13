"""
https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/description/?envType=daily-question&envId=2024-01-05
2385. Amount of Time for Binary Tree to Be Infected
"""
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


parents = {}


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        if root is None:
            return -1
        node = find_start(root, None, start)
        queue = deque()
        queue.append(node)
        seen = set([node.val])
        minutes = -1
        while queue:
            minutes += 1
            count = len(queue)
            for _ in range(count):
                node = queue.popleft()
                # print(f"node: {node.val}")
                parent = parents.get(node)
                if parent and parent.val not in seen:
                    # print(f"    has parent: {parent.val}")
                    seen.add(parent.val)
                    queue.append(parent)
                if node.left and node.left.val not in seen:
                    # print(f"    has left: {node.left.val}")
                    seen.add(node.left.val)
                    queue.append(node.left)
                if node.right and node.right.val not in seen:
                    # print(f"    has right: {node.right.val}")
                    seen.add(node.right.val)
                    queue.append(node.right)
        return minutes


def find_start(
    node: Optional[TreeNode], parent: Optional[TreeNode], start: int
) -> TreeNode:
    if node is None:
        return None
    parents[node] = parent
    if node.val == start:
        return node
    left = find_start(node.left, node, start)
    if left is not None:
        return left
    return find_start(node.right, node, start)
