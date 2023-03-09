"""
https://leetcode.com/problems/linked-list-cycle-ii/
142. Linked List Cycle II
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.
"""
from typing import Optional, Set

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """Two pointer approach"""
        if head is None or head.next is None:
            return None

        slow = fast = head
        while slow and fast and fast.next:
            # Move slow and fast pointers
            slow, fast = slow.next, fast.next.next
            # If the two pointers meet, we can say there is a cycle
            if slow == fast:
                break

        # If fast and slow is not the same -> fast points to None and there is no cycle
        if fast != slow:
            return None

        slow = head
        while slow and fast:
            if slow == fast:
                break
            slow, fast = slow.next, fast.next

        if slow == fast:
            return slow
        return None

        # """Intuitive approach even better"""
        # s: Set[ListNode] = set()

        # while head is not None:
        # if head in s:
        # return head
        # s.add(head)
        # head = head.next
        # return None
