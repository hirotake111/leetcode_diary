"""
https://leetcode.com/problems/find-largest-value-in-each-tree-row/
515. Find Largest Value in Each Tree Row
"""
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        answer, queue, MIN = [], deque(), -(2**31 + 1)
        if root:
            queue.append(root)

        i = -1
        while queue:
            l, i = len(queue), i + 1
            answer.append(MIN)  # set the minimum value
            for _ in range(l):
                node = queue.popleft()
                answer[i] = max(answer[i], node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return answer
