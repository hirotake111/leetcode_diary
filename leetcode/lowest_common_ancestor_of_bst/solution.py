# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: TreeNode, p: TreeNode, q: TreeNode
    ) -> "TreeNode":
        a = b = prev = root

        while a == b:
            if p.val < a.val:
                prev = a
                a = a.left
            elif a.val < p.val:
                prev = a
                a = a.right
            else:
                return a

            if q.val < b.val:
                b = b.left
            elif b.val < q.val:
                b = b.right
            else:
                return b

        return prev
