from unittest import main, TestCase
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"<{self.val}>"


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None:
            return head
        l = 1
        node = head
        # calculate length of ListNode
        while node.next:
            node = node.next
            l += 1
        target = l - n
        current = 0
        node = head
        prev: Optional[ListNode] = None
        if target == 0:
            # remove first node
            head = node.next
            prev = head
            node = head
        if node is None:
            return head
        while node and node.next:
            if target == current:
                # remove node
                prev.next = node.next
                node = prev
                current += 1
            prev = node
            node = node.next
            current += 1
        if target == current:
            prev.next = None
        return head


def list_to_node(arr: List[int]) -> ListNode:
    head: ListNode = None
    prev: ListNode = None
    for val in arr:
        node = ListNode(val=val)
        if head is None:
            head = node
        if prev:
            prev.next = node
        prev = node
    return head


def node_to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    if node is None:
        return result
    result.append(node.val)
    while node.next:
        node = node.next
        result.append(node.val)
    return result


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        # self.assertEqual(node_to_list(list_to_node([1, 4, 3, 2])), [1, 4, 3, 2])
        # self.assertEqual(
        #     node_to_list(
        #         self.s.removeNthFromEnd(head=list_to_node([1, 2, 3, 4, 5]), n=1)
        #     ),
        #     [1, 2, 3, 4],
        # )
        # self.assertEqual(
        #     node_to_list(
        #         self.s.removeNthFromEnd(head=list_to_node([1, 2, 3, 4, 5]), n=2)
        #     ),
        #     [1, 2, 3, 5],
        # )
        # self.assertEqual(
        #     node_to_list(
        #         self.s.removeNthFromEnd(head=list_to_node([1, 2, 3, 4, 5]), n=3)
        #     ),
        #     [1, 2, 4, 5],
        # )
        # self.assertEqual(
        #     node_to_list(
        #         self.s.removeNthFromEnd(head=list_to_node([1, 2, 3, 4, 5]), n=4)
        #     ),
        #     [1, 3, 4, 5],
        # )
        # self.assertEqual(
        #     node_to_list(
        #         self.s.removeNthFromEnd(head=list_to_node([1, 2, 3, 4, 5]), n=5)
        #     ),
        #     [2, 3, 4, 5],
        # )
        self.assertEqual(
            node_to_list(self.s.removeNthFromEnd(head=list_to_node([1]), n=1)),
            [],
        )


if __name__ == "__main__":
    main()
