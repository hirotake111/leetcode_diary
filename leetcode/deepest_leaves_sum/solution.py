from typing import List, Optional, Tuple
from unittest import TestCase, main

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self) -> str:
        return f"<{self.val}>"


def list_to_node(arr: List[Optional[int]]) -> TreeNode:
    queue: List[TreeNode] = [TreeNode(val=arr[0])]
    root = queue[0]
    i, l = 0, len(arr)
    while len(queue) > 0:
        node = queue.pop(0)
        i += 1
        if i == l:
            break
        if arr[i] is not None:
            node.left = TreeNode(val=arr[i])
            queue.append(node.left)
        i += 1
        if i == l:
            break
        if arr[i] is not None:
            node.right = TreeNode(val=arr[i])
            queue.append(node.right)
    return root


def node_to_list(node: TreeNode) -> List[Optional[int]]:
    arr: List[Optional[int]] = []
    queue: List[Optional[TreeNode]] = [node]
    while len(queue) > 0:
        n = queue.pop(0)
        if n is None:
            arr.append(None)
            continue
        arr.append(n.val)
        if n.left is not None:
            queue.append(n.left)
        else:
            queue.append(None)
        if n.right is not None:
            queue.append(n.right)
        else:
            queue.append(None)
    for i in range(len(arr) - 1, -1, -1):
        if arr[i] is not None:
            break
    return arr[: i + 1]


class Solution:
    ans: int
    deepest: int

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.deepest = 0

        def dfs(node: Optional[TreeNode], current: int):
            if node is None:
                return

            if node.left is not None or node.right is not None:
                if node.left is not None:
                    dfs(node.left, current + 1)
                if node.right is not None:
                    dfs(node.right, current + 1)
                return

            if current == self.deepest:
                self.ans += node.val
            elif current > self.deepest:
                self.ans = node.val
                self.deepest = current

        dfs(root, 0)
        return self.ans


class TestSolution(TestCase):
    def test_solution(self):
        s = Solution()
        arr = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]
        node = list_to_node(arr)
        self.assertEqual(node_to_list(node), arr)
        data: List[Tuple[List[Optional[int]], int]] = [
            ([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8], 15),
            ([6, 7, 8, 2, 7, 1, 3, 9, None, 1, 4, None, None, None, 5], 19),
        ]
        for input, expected in data:
            root = list_to_node(input)
            self.assertEqual(s.deepestLeavesSum(root), expected)


if __name__ == "__main__":
    main()
