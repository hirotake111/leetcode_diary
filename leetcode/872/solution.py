"""
https://leetcode.com/problems/leaf-similar-trees/description/?envType=daily-question&envId=2024-01-05
872. Leaf-Similar Trees
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return dfs(root1) == dfs(root2)


def dfs(node: Optional[TreeNode]) -> List[int]:
    if node is None:
        return []
    if node.left is None and node.right is None:
        return [node.val]
    arr = []
    if node.left:
        arr += dfs(node.left)
    if node.right:
        arr += dfs(node.right)
    return arr
