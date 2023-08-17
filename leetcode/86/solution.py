"""
https://leetcode.com/problems/partition-list/
86. Partition List
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        smaller, larger = [], []
        node = head
        while node:
            if node.val < x:
                smaller.append(node)
            else:
                larger.append(node)
            node = node.next

        new_head: Optional[ListNode] = None
        prev: Optional[ListNode] = None
        for node in smaller + larger:
            if prev is None:
                new_head = prev = node
            else:
                prev.next = node
                prev = node
            node.next = None

        return new_head
