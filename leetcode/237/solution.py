"""
https://leetcode.com/problems/delete-node-in-a-linked-list/
237. Delete Node in a Linked List
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node: ListNode):
        next_node = node.next
        node.val = next_node.val
        node.next = next_node.next
        next_node.next = None
        del next_node
