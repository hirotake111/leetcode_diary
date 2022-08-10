from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def func(low: int, high: int) -> Optional[TreeNode]:
            if low == high:
                return TreeNode(val=nums[low])
            if low + 1 == high:
                return TreeNode(val=nums[high], left=TreeNode(val=nums[low]))
            mid = low + (high - low) // 2
            node = TreeNode(val=nums[mid])
            node.left = func(low, mid - 1)
            node.right = func(mid + 1, high)
            return node

        return func(0, len(nums) - 1)
