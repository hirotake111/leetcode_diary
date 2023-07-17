"""
https://leetcode.com/problems/add-two-numbers-ii/description/
445. Add Two Numbers II

You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        summary = self.calc(l1) + self.calc(l2)

        # Edge case
        if summary == 0:
            return ListNode(0)

        # Create a new linked list from tail to head
        node = prev = None
        while summary:
            summary, remainder = divmod(summary, 10)
            node = ListNode(remainder)
            node.next = prev
            prev = node

        return node

    def calc(self, node: Optional[ListNode]) -> int:
        result = 0
        while node:
            result = result * 10 + node.val
            node = node.next
        return result
