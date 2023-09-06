"""
https://leetcode.com/problems/split-linked-list-in-parts/
725. Split Linked List in Parts
"""
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(
        self, head: Optional[ListNode], k: int
    ) -> List[Optional[ListNode]]:
        answer: List[Optional[ListNode]] = [None] * k

        # Create a list of node
        node = head
        arr = []
        while node:
            arr.append(node)
            node = node.next

        n, extra = divmod(len(arr), k)
        i = 0  # index of arr
        for j in range(k):  # index of answer
            if i >= len(arr):
                break
            answer[j] = arr[i]
            # i - 1 points to the tail of answer[j] -> remove .next
            arr[i - 1].next = None
            # Update i. And increment it by 1 if needed
            i += n + (1 if extra > 0 else 0)
            # Update extra
            extra = max(extra - 1, 0)

        return answer
