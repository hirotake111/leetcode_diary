from typing import Optional, List

"""
inorder: Left > Root > Right
preorder: Root > Left > Right
postorer: Left > Right > Root
"""
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # one liner approach
        def dfs(node: Optional[TreeNode]) -> List[int]:
            return [] if node is None else dfs(node.left) + [node.val] + dfs(node.right)

        return dfs(root)

        # intuitive approach
        # answer: List[int] = []
        # if root is None:
        # return []

        # def dfs(node: TreeNode) -> None:
        # if node.left:
        # dfs(node.left)
        # answer.append(node.val)
        # if node.right:
        # dfs(node.right)

        # dfs(root)
        # return answer
