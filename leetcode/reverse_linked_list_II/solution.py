from tkinter import W
from typing import List, Optional, Tuple
from unittest import TestCase, main

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return self.val

    def __str__(self) -> str:
        return self.val


def list_to_node(l: List[int]) -> Optional[ListNode]:
    head = None
    prev = None
    for i in l:
        node = ListNode(val=i)
        if head is None:
            head = node
        else:
            prev.next = node
        prev = node

    return head


def node_to_list(node: Optional[ListNode]) -> List[int]:
    l: List[int] = []
    while True:
        if node is None:
            return []
        l.append(node.val)
        if node.next is None:
            break
        node = node.next
    return l


class Solution:
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if left == right:
            return head

        node = ListNode(val=0, next=head)
        prev_left: Optional[ListNode] = None
        prev_right: Optional[ListNode] = None

        while node.next != None:
            next = node.next
            if next.val == left:
                prev_left = node
            if next.val == right:
                prev_right = node
                break
            node = node.next
        if prev_left is None or prev_right is None:
            raise Exception("Failed to identify either node a or b")
        if prev_left.next == prev_right:
            # left and right are neighbour
            new_left, new_right = prev_right.next, prev_left.next
            new_right.next, new_left.next = new_left, prev_right.next

        else:
            new_left, new_right = prev_right.next, prev_left.next
            prev_left.next, prev_right.next = prev_right.next, prev_left.next
            new_left.next, new_right.next = new_right.next, new_left.next

        return head


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[int], int, int, List[int]]] = [
        ([1, 2, 3, 4, 5], 2, 3, [1, 3, 2, 4, 5]),
        ([1, 2, 3, 4, 5], 2, 4, [1, 4, 3, 2, 5]),
        ([5], 1, 1, [5]),
    ]

    def test_solution(self):
        for l, left, right, expected in self.data:
            head = list_to_node(l)
            result = self.s.reverseBetween(head, left, right)
            self.assertEqual(node_to_list(result), expected)


if __name__ == "__main__":
    main()
