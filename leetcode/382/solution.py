"""
https://leetcode.com/problems/linked-list-random-node/
382. Linked List Random Node
Given a singly linked list, return a random node's value from the linked list. Each node must have the same probability of being chosen.

Implement the Solution class:

Solution(ListNode head) Initializes the object with the head of the singly-linked list head.
int getRandom() Chooses a node randomly from the list and returns its value. All the nodes of the list should be equally likely to be chosen.
"""
from typing import List, Optional
import random

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    nodes: List[ListNode]

    def __init__(self, head: Optional[ListNode]):
        self.nodes = []
        while head:
            self.nodes.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.nodes)
