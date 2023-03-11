"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
109. Convert Sorted List to Binary Search Tree
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height-balanced binary search tree.
"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        """Two pointer approach"""
        if head is None:
            return None

        return self.get_child(head, ListNode(0))

    def get_child(self, head: ListNode, tail: ListNode) -> TreeNode:
        if head.next is None or head == tail:
            # We have only one ListNode -> return it
            return TreeNode(head.val)

        slow = fast = prev = head
        # Let fast get to the last node
        while fast.next and fast != tail:
            prev = slow
            slow, fast = slow.next, fast.next
            if fast != tail and fast.next:
                fast = fast.next

        # Now slow should point to root of given ListNode
        left = self.get_child(head, prev)
        if slow == fast:
            # There is no right node
            return TreeNode(slow.val, left)
        # slow != fast -> there is at least one right node
        right = self.get_child(slow.next, fast)
        return TreeNode(slow.val, left, right)


if __name__ == "__main__":
    solution = Solution()
    solution.sortedListToBST(
        ListNode(-10, ListNode(-3, ListNode(0, ListNode(5, ListNode(9)))))
    )
