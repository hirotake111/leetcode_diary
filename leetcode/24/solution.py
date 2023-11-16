from typing import List, Optional
from unittest import main, TestCase


class ListNode:
    # Definition for singly-linked list.
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"<val:{self.val}>"

    def __repr__(self) -> str:
        return f"<val:{self.val}>"


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        prev: ListNode = None
        prev2: ListNode = None
        flag = False
        while node:
            if flag:
                # suppose node is now d:
                # a.next = d
                if prev2:
                    prev2.next = node
                else:  # this must be the first swap -> update head
                    head = node
                # c.next = e
                prev.next = node.next
                # d.next = c
                node.next = prev
                # update flag
                flag = not flag
                # prev2 -> d
                prev2 = node
                # prev -> c (c remains prev)
                # next node -> e
                node = prev.next
            else:
                # now we will not switch nodes
                flag = not flag
                # suppose node is now c:
                # prev2 -> a
                if prev:  # this is not the 1st element
                    prev2 = prev
                # prev -> c
                prev = node
                # next node -> d
                node = node.next
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
    ans = []
    while node:
        ans.append(node.val)
        node = node.next
    return ans


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        l = [1, 2, 3, 4]
        self.assertEqual(node_to_list(list_to_node(l)), l)
        nodes = list_to_node([1, 2, 3, 4])
        expected = [2, 1, 4, 3]
        self.assertEqual(node_to_list(self.s.swapPairs(nodes)), expected)
        nodes = list_to_node([])
        expected = []
        self.assertEqual(node_to_list(self.s.swapPairs(nodes)), expected)
        nodes = list_to_node([1])
        expected = [1]
        self.assertEqual(node_to_list(self.s.swapPairs(nodes)), expected)
        nodes = list_to_node([1, 2, 3, 4, 5, 6, 7, 8])
        expected = [2, 1, 4, 3, 6, 5, 8, 7]
        self.assertEqual(node_to_list(self.s.swapPairs(nodes)), expected)


if __name__ == "__main__":
    main()
