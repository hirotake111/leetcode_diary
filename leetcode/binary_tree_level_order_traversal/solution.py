from queue import Queue
from collections import deque
from typing import Deque, Optional, List, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        answer: List[List[int]] = []
        queue: Queue[TreeNode] = Queue()
        queue.put(root)

        while queue:
            sub_arr: List[int] = []
            for _ in range(queue.qsize()):
                node = queue.get()
                sub_arr += [node.val]
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)

            answer.append(sub_arr)

        return answer
        # if root is None:
        # return []

        # answer: List[List[int]] = []
        # d: Deque[TreeNode] = deque()
        # d.append(root)

        # while d:
        # sub_arr: List[int] = []
        # for _ in range(len(d)):
        # node = d.popleft()
        # sub_arr += [node.val]
        # if node.left:
        # d.append(node.left)
        # if node.right:
        # d.append(node.right)

        # answer.append(sub_arr)

        # return answer

        # first approach
        # if root is None:
        # return []
        # answer: List[List[int]] = []
        # queue: Queue[Tuple[TreeNode, int]] = Queue()
        # queue.put((root, 0))

        # while not queue.empty():
        # node, index = queue.get()
        # if len(answer) == index:
        # answer.append([node.val])
        # else:
        # answer[index] += [node.val]

        # if node.left:
        # queue.put((node.left, index + 1))
        # if node.right:
        # queue.put((node.right, index + 1))

        # return answer
