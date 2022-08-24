from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        result = [head.val]
        node = head.next
        while node:
            result.append(node.val)
            node = node.next
        return result == result[::-1]
