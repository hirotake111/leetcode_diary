"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
230. Kth Smallest Element in a BST
"""
from typing import List, Optional
from unittest import main, TestCase


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"<{self.val}>"


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr: List[int] = []

        def dfs_inorder(node: Optional[TreeNode]):
            if node is None:
                return
            dfs_inorder(node.left)
            arr.append(node.val)
            dfs_inorder(node.right)

        dfs_inorder(root)
        return arr[k - 1]


class TestSolution(TestCase):
    s = Solution()

    def test_s(self):
        root = [3, 1, 4, None, 2]
        input = list_to_bst(root)
        expected = 1
        self.assertEqual(self.s.kthSmallest(input, 1), expected)
        root = [5, 3, 6, 2, 4, None, None, 1]
        input = list_to_bst(root)
        expected = 3
        self.assertEqual(self.s.kthSmallest(input, 3), expected)


def list_to_bst(arr: List[int]) -> TreeNode:
    root = TreeNode(val=arr[0])
    queue: List[Optional[TreeNode]] = [root]
    i, l = 1, len(arr)
    while i < l:
        node = queue.pop()
        if node is None:
            i += 2
            continue
        # add a new node to left node
        node.left = TreeNode(val=arr[i]) if arr[i] else None
        queue.insert(0, node.left)
        i += 1
        if i == l:
            break
        # add a new node to right node
        node.right = TreeNode(val=arr[i]) if arr[i] else None
        queue.insert(0, node.right)
        i += 1

    return root


if __name__ == "__main__":
    main()
