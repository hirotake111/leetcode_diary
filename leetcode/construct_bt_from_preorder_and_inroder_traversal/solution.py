from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        l = len(inorder)
        if l == 0:
            return None
        root = TreeNode(val=preorder[0])

        if l == 1:
            return root

        # find root index for root node in inorder list
        i = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1 : i + 1], inorder[:i])
        root.right = self.buildTree(preorder[i + 1 :], inorder[i + 1 :])
        return root


if __name__ == "__main__":
    s = Solution()
    s.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
