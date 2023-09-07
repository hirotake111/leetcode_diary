"""
https://leetcode.com/problems/reverse-linked-list-ii/
92. Reverse Linked List II
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        # Create an array that contains a dummy head + all nodes
        arr = [ListNode(0, head)]
        while head:
            arr.append(head)
            head = head.next

        # Rearrange the array
        arr = arr[:left] + list(reversed(arr[left : right + 1])) + arr[right + 1 :]

        # Re-combine all the nodes
        prev = None
        for i, node in enumerate(arr):
            if prev is not None:
                prev.next = node
            prev = node

        # Don't forget to nullify prev.next (otherwise it could become a cyclic node)
        if prev is not None:
            prev.next = None

        # Disconnect dummy head and return head
        head = arr[0].next
        arr[0].next = None
        return head
