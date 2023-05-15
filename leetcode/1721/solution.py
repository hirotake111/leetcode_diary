"""
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/submissions/950502043/
1721. Swapping Nodes in a Linked List

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        # Convert the list into an array
        while head:
            arr.append(head)
            head = head.next

        # Swap
        arr[k - 1].val, arr[-k].val = arr[-k].val, arr[k - 1].val

        return arr[0]
