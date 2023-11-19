"""
https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
2095. Delete the Middle Node of a Linked List
"""
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr: List[ListNode] = []
        node = head
        while node:
            arr.append(node)
            node = node.next

        n = len(arr)
        if n < 1:
            return None

        if n == 2:
            arr[0].next = None
            return head

        mid = n // 2
        arr[mid - 1].next = arr[mid + 1]
        arr[mid].next = None
        return head
