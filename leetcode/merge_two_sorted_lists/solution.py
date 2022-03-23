from unittest import main, TestCase
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"<{self.val}>"


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        head: Optional[ListNode] = None
        prev: Optional[ListNode] = None

        while list1 is not None or list2 is not None:
            if list1 is None:  # only list2 exists
                node = ListNode(val=list2.val)
                list2 = list2.next
            elif list2 is None:  # only list1 exists
                node = ListNode(val=list1.val)
                list1 = list1.next
            elif list1.val <= list2.val:
                node = ListNode(val=list1.val)
                list1 = list1.next
            else:  # list1.val > list2.val
                node = ListNode(val=list2.val)
                list2 = list2.next
            if head is None:  # set head
                head = node
            if prev:  # set prev.next
                prev.next = node
            prev = node

        return head


def list_to_node(l: List[int]) -> ListNode:
    head: Optional[ListNode] = None
    prev: Optional[ListNode] = None
    for val in l:
        node = ListNode(val=val)
        if head is None:
            head = node
        if prev:
            prev.next = node
        prev = node
    return head


def node_to_list(node: ListNode) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(node_to_list(list_to_node([2, 3, 4, 5])), [2, 3, 4, 5])
        node1 = list_to_node([1, 2, 4])
        node2 = list_to_node([1, 3, 4])
        expected = [1, 1, 2, 3, 4, 4]
        self.assertEqual(node_to_list(self.s.mergeTwoLists(node1, node2)), expected)
        node1 = list_to_node([])
        node2 = list_to_node([])
        expected = []
        self.assertEqual(node_to_list(self.s.mergeTwoLists(node1, node2)), expected)
        node1 = list_to_node([])
        node2 = list_to_node([0])
        expected = [0]
        self.assertEqual(node_to_list(self.s.mergeTwoLists(node1, node2)), expected)


if __name__ == "__main__":
    main()
