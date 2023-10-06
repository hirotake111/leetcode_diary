"""
https://leetcode.com/problems/path-sum/
112. Path Sum
"""
from typing import Optional
from unittest import TestCase, main


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    found = False

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if self.found or root is None:
            return False

        targetSum -= root.val
        # leaf
        if root.left is None and root.right is None and targetSum == 0:
            self.found = True
            return True

        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(
            root.right, targetSum
        )


if __name__ == "__main__":
    main()


class Test(TestCase):
    def test_solution(self):
        s = Solution()
        root = TreeNode(1, TreeNode(2))
        self.assertEqual(s.hasPathSum(root, 1), False)
