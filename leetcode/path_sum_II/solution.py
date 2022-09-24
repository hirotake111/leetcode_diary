from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        answer: List[List[int]] = []

        def dfs(node: Optional[TreeNode], arr: List[int], total: int) -> None:
            if node is None:
                return

            total += node.val
            if targetSum == total and node.left is None and node.right is None:
                answer.append(arr + [node.val])
                return

            dfs(node.left, arr + [node.val], total)
            dfs(node.right, arr + [node.val], total)

        dfs(root, [], 0)
        return answer
