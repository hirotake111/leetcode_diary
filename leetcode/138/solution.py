"""
https://leetcode.com/problems/copy-list-with-random-pointer/
138. Copy List with Random Pointer
"""
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(
        self, x: int, next: Optional["Node"] = None, random: Optional["Node"] = None
    ):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if head is None:
            return None

        arr, new_arr, hm = [], [], {}
        node: Optional[Node] = head
        prev = None
        i = 0
        while node:
            arr.append(node)
            new_arr.append(Node(node.val))
            if prev:
                prev.next = new_arr[-1]
            prev = new_arr[-1]
            hm[node] = i
            i += 1
            node = node.next

        for i, node in enumerate(arr):
            if node.random:
                random_idx = hm[node.random]
                new_arr[i].random = new_arr[random_idx]

        return new_arr[0]
