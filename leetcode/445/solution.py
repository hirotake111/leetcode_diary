"""
https://leetcode.com/problems/add-two-numbers-ii/description/
445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        arr1, arr2 = self.get_arr(l1), self.get_arr(l2)
        diff = len(arr2) - len(arr1)
        if diff < 0:
            # arr1 is longer than arr2
            arr1, arr2 = arr2, arr1
        # Now arr2 is longer than arr1 -> perform padding
        arr1 = [0] * abs(diff) + arr1
        # Add arr1 + arr2
        carry_over = 0
        for i in range(len(arr1) - 1, -1, -1):
            n, r = divmod(arr1[i] + arr2[i] + carry_over, 10)
            arr1[i] = r
            carry_over = n
        if carry_over:
            arr1 = [1] + arr1
        # Create a new linked list
        root = prev = None
        for n in arr1:
            node = ListNode(n)
            if root is None:
                root = prev = node
            else:
                prev.next = node
                prev = node

        return root

    def get_arr(self, node: ListNode) -> List[int]:
        arr = []
        while True:
            if node is None:
                break
            arr.append(node.val)
            node = node.next
        return arr
