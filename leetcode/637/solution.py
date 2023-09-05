"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/
637. Average of Levels in Binary Tree
"""
from queue import Queue
from typing import List, Optional, Tuple


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        answer: List[float] = []
        queue: Queue[TreeNode] = Queue()
        queue.put(root)

        while not queue.empty():
            size = current = queue.qsize()
            total = 0
            while 0 < current:
                node = queue.get()
                total += node.val
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)
                current -= 1
            answer.append(total / size)

        return answer
