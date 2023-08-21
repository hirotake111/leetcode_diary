"""
https://leetcode.com/problems/add-two-numbers/
2. Add Two Numbers
"""
from typing import List, Optional
from unittest import TestCase, main


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val}"


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        carry = 0
        entry = ListNode()
        node = entry
        while True:
            if l1 is None and l2 is None:
                break

            if l1 is None:
                # we only have l2 now
                c, val = divmod(l2.val + carry, 10)
                node.val = val
                carry = c
                if l2.next is None:
                    break
                l2 = l2.next
                node.next = ListNode()
                node = node.next
                continue

            if l2 is None:
                # we only have l1 now
                c, val = divmod(l1.val + carry, 10)
                node.val = val
                carry = c
                if l1.next is None:
                    break
                l1 = l1.next
                node.next = ListNode()
                node = node.next
                continue

            # we have l1 and l2 here
            c, val = divmod(l1.val + l2.val + carry, 10)
            carry = c
            node.val = val
            if l1.next is None and l2.next is None:
                break
            l1 = l1.next
            l2 = l2.next
            node.next = ListNode()
            node = node.next

        if carry == 1:
            node.next = ListNode()
            node.next.val = 1

        return entry


def list_to_node(l: List[int]):
    entry = ListNode()
    node = entry
    for i in range(len(l)):
        node.val = l[i]
        if i != len(l) - 1:
            node.next = ListNode()
            node = node.next

    return entry


def printNode(l: ListNode):
    while True:
        print(l.val)
        l = l.next
        if l is None:
            break


def node_to_list(l: ListNode):
    result = []
    while True:
        result.append(l.val)
        l = l.next
        if l is None:
            break

    return result


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
class TestSolution(TestCase):
    def setUp(self) -> None:
        self.s = Solution()

    def test_getNode(self):
        node = list_to_node([1, 2, 3])
        self.assertEqual(node_to_list(node), [1, 2, 3])

    def test_input(self):
        l1 = list_to_node([2, 4, 3])
        l2 = list_to_node([5, 6, 4])
        node = self.s.addTwoNumbers(l1, l2)
        self.assertEqual(node_to_list(node), [7, 0, 8])

    def test_input2(self):
        l1 = list_to_node([9, 9, 9, 9, 9, 9, 9])
        l2 = list_to_node([9, 9, 9, 9])
        node = self.s.addTwoNumbers(l1, l2)
        self.assertEqual(node_to_list(node), [8, 9, 9, 9, 0, 0, 0, 1])


if __name__ == "__main__":
    main()
