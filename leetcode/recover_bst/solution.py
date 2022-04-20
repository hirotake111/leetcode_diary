from turtle import right
from typing import List, Optional
from unittest import main, TestCase
from queue import Queue

"""
    6
2       4
     1
    6
2       1
     4
    2
1      6
     4
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return self.val

    def __str__(self) -> str:
        return self.val


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def bfs(node: Optional[TreeNode], high: TreeNode, low: TreeNode) -> bool:
            if node is None:
                return True
            if node.left:
                if not low.val < node.left.val:
                    # swap value
                    low.val, node.left.val = node.left.val, low.val
                    return False
                if not node.left.val < node.val:
                    # swap values
                    node.val, node.left.val = node.left.val, node.val
                    return False
            if node.right:
                if not (node.right.val < high.val):
                    high.val, node.right.val = node.right.val, high.val
                    return False
                if not (node.val < node.right.val):
                    # swap
                    node.val, node.right.val = node.right.val, node.val
                    return False

            return bfs(node.left, node, low) and bfs(node.right, high, node)

        if root is None:
            return

        while not bfs(root, TreeNode(float("inf")), TreeNode(float("-inf"))):
            pass


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        # input = [1, 3, None, None, 2]
        # self.assertEqual(bst_to_list(list_to_bst(input)), input)

        # input = [1, 3, None, None, 2]
        # expected = [3, 1, None, None, 2]
        # root = list_to_bst(input)
        # self.s.recoverTree(root)
        # self.assertEqual(bst_to_list(root), expected)

        input = [3, 1, 4, None, None, 2]
        expected = [2, 1, 4, None, None, 3]
        root = list_to_bst(input)
        self.s.recoverTree(root)
        self.assertEqual(bst_to_list(root), expected)


def list_to_bst(arr: List[Optional[int]]) -> Optional[TreeNode]:
    root = TreeNode(val=arr[0])
    queue: List[Optional[TreeNode]] = [root]
    i, l = 0, len(arr)
    while len(queue) > 0:
        node = queue.pop()
        if node is None:
            i += 2
            continue

        i += 1
        if i >= l:
            break
        node.left = TreeNode(val=arr[i]) if arr[i] is not None else None
        queue.insert(0, node.left)
        i += 1
        if i >= l:
            break
        node.right = TreeNode(val=arr[i]) if arr[i] is not None else None
        queue.insert(0, node.right)
    return root


def bst_to_list(root: Optional[TreeNode]) -> List[Optional[int]]:
    arr: List[Optional[int]] = []
    queue: List[Optional[TreeNode]] = [root]
    while len(queue) > 0:
        node = queue.pop()
        if node is None:
            arr.append(None)
            continue
        else:
            arr.append(node.val)
            queue.insert(0, node.left)
            queue.insert(0, node.right)
    for j in range(len(arr) - 1, 0, -1):
        if arr[j] is not None:
            break
    return arr[: j + 1]


if __name__ == "__main__":
    main()
