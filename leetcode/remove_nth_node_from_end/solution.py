from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:  # edge case
            return None

        arr: List[ListNode] = []
        node = head

        while node:
            arr.append(node)
            node = node.next

        count = len(arr)
        last, target = count - 1, count - n
        prev = target - 1

        if target == 0:  # remove the first node
            return head.next

        if target == last:  # remove the last node from previous one
            arr[prev].next = None
            return head

        # else
        arr[prev].next = arr[target].next
        arr[target].next = None
        return head
