from typing import List, Tuple
from queue import Queue

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: Node) -> List[List[int]]:
        if root is None:
            return []
        q, answer = [root], []
        while q:
            answer.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return answer

        # q: Queue[Tuple[Node, int]] = Queue()
        # answer: List[List[int]] = [[]]
        # if root is None:
        #     return []
        # q.put((root, 0))

        # while not q.empty():
        #     node, idx = q.get()
        #     if idx <= len(answer) - 1:
        #         answer[idx] += [node.val]
        #     else:
        #         answer += [[node.val]]

        #     for child in node.children:
        #         q.put((child, idx + 1))
        # return answer
