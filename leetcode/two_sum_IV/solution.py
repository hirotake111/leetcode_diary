from optparse import Option
from queue import Queue
from typing import Optional, Set


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        """BFS approach"""
        nums: Set[int] = set()
        queue: Queue[Optional[TreeNode]] = Queue()

        queue.put(root)
        while not queue.empty():
            node = queue.get()
            if node is None:
                continue
            if k - node.val in nums:
                return True
            nums.add(node.val)
            queue.put(node.left)
            queue.put(node.right)

        return False
        # """DFS approach"""
        # nums: Set[int] = set()

        # def dfs(node: Optional[TreeNode]) -> bool:
        # if node is None:
        # return False
        # if k - node.val in nums:
        # return True
        # nums.add(node.val)
        # return dfs(node.left) or dfs(node.right)

        # return dfs(root)
