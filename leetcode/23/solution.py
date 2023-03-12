"""
https://leetcode.com/problems/merge-k-sorted-lists/
23. Merge k Sorted Lists
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
"""
from typing import List, Optional
from heapq import heappush, heappop

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        queue: List[int] = []

        # Push all the values in list into heap queue
        for l in lists:
            while l:
                heappush(queue, l.val)
                l = l.next

        # Edge case
        if len(queue) == 0:
            return None

        # Pop each element from heap queue and create a list node
        head = node = ListNode(heappop(queue))
        while queue:
            node.next = ListNode(heappop(queue))
            node = node.next

        return head
