"""
https://leetcode.com/problems/linked-list-cycle/?envType=daily-question&envId=2023-09-04
141. Linked List Cycle
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next

        return False
