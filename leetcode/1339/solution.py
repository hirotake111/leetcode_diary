"""
1339. Maximum Product of Splitted Binary Tree
https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
"""
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    total: int = 0
    product: int = 0

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def get_total(node: Optional[TreeNode]) -> int:
            """Recursively adds values of each node and returns total value of all nodes in the end"""
            if node is None:
                return 0
            return get_total(node.left) + get_total(node.right) + node.val

        def get_product(node: Optional[TreeNode]) -> int:
            """Recursively get the sum of nodes and update self.product if necessary"""
            if node is None:
                return 0

            # Get sum of left node, right node, and its value
            current_sum = get_product(node.left) + get_product(node.right) + node.val
            # Calculate the product
            product = current_sum * (self.total - current_sum)
            # If the product is larger than the current one, replace it
            self.product = max(self.product, product)
            # return sum of current node for future use
            return current_sum

        # Get total value of all nodes
        self.total = get_total(root)
        # Update self.product
        get_product(root)
        # Don't forget to modulo 10**9 + 7
        return self.product % 1000000007
