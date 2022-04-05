from typing import List, Optional, cast
from unittest import main, TestCase


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        if self.next is None:
            return self.val
        return f"{self.val}-{self.next}"

    def __str__(self) -> str:
        if self.next is None:
            return self.val
        return f"{self.val}-{self.next}"


class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        O(n) solution
        """
        # prev: Optional[ListNode] = None
        # a1: Optional[ListNode] = None
        # a2: Optional[ListNode] = None
        # b1: Optional[ListNode] = None
        # b2: Optional[ListNode] = None

        # if head is None:
        #     return head
        # idx = 1
        # node = head
        # # count the num of nodes, and identify a1 and a2
        # while node:
        #     if idx == k:
        #         a2 = node
        #         if k != 1:
        #             a1 = prev
        #     prev = node
        #     node = node.next
        #     idx += 1

        # j = idx - k
        # node = head
        # idx = 1

        # # identify b1 and b2
        # while node:
        #     if idx == j:
        #         b2 = node
        #         if j != 1:
        #             b1 = prev
        #     prev = node
        #     node = node.next
        #     idx += 1

        # if a2 == b2:
        #     # must be only one element
        #     return head

        # if k > j:
        #     # swap a and b
        #     a1, b1 = b1, a1
        #     a2, b2 = b2, a2

        # tmp = a2.next
        # a2.next = b2.next
        # if a2 == b1:
        #     # i and j is neighbor
        #     b2.next = a2
        # else:
        #     # not neighbor
        #     b2.next = tmp
        #     b1.next = a2

        # if a1:
        #     a1.next = b2
        # else:
        #     head = b2

        # return head
        """
        sliding window solution
        """
        # first = slow = fast = head
        # i = 0
        # while fast.next or k - 1 > i:

        #     if k - 1 > i:
        #         i += 1
        #         first = first.next
        #     else:
        #         slow = slow.next

        #     if fast.next:
        #         fast = fast.next
        # # swap
        # first.val, slow.val = slow.val, first.val
        # return head
        """
        simpler sliding window solution
        O(n)
        O(1)
        """
        # slow = fast = head
        # # find kth node
        # for _ in range(k - 1):
        #     fast = fast.next
        # # this also must be fist element
        # first = fast
        # # find kth node from right using sliding window approach
        # while fast.next:
        #     fast = fast.next
        #     slow = slow.next

        # # swap only vlaues
        # first.val, slow.val = slow.val, first.val
        # return head
        """
        simpler siliding window approach (swapping nodes)
        """
        # add dummy nodes first
        dummy = pre_right = pre_left = ListNode(val=0, next=head)
        left = right = head

        # find kth node
        for _ in range(k - 1):
            pre_left = right
            right = right.next
        # this should be fast node too
        fast = right
        while fast.next:
            fast = fast.next
            pre_right = pre_right.next
            left = left.next
        # swap nodes
        pre_right.next, pre_left.next = right, left
        left.next, right.next = right.next, left.next
        return dummy.next


def list_to_node(nums: List[int]) -> ListNode:
    head: Optional[ListNode] = None
    prev = ListNode()

    for i in range(len(nums)):
        node = ListNode(val=nums[i])
        if head is None:
            head = node
        else:
            prev.next = node
        prev = node

    return cast(ListNode, head)


def node_to_list(node: ListNode) -> List[int]:
    nums: List[int] = []
    while node is not None:
        nums.append(node.val)
        node = node.next
    return nums


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        # l = [1, 2, 3, 4, 5]
        # self.assertEqual(node_to_list(list_to_node(l)), l)
        # node = list_to_node([1, 2, 3, 4, 5])
        # swapped = self.s.swapNodes(node, 2)
        # self.assertEqual(node_to_list(swapped), [1, 4, 3, 2, 5])
        node = list_to_node([7, 9, 6, 6, 7, 8, 3, 0, 9, 5])
        swapped = self.s.swapNodes(node, 5)
        self.assertEqual(node_to_list(swapped), [7, 9, 6, 6, 8, 7, 3, 0, 9, 5])
        # node = list_to_node([100, 90])
        # swapped = self.s.swapNodes(node, 2)
        # self.assertEqual(node_to_list(swapped), [90, 100])
        # node = list_to_node([100, 90])
        # swapped = self.s.swapNodes(node, 1)
        # self.assertEqual(node_to_list(swapped), [90, 100])
        # node = list_to_node([80, 46, 66, 35, 64])
        # swapped = self.s.swapNodes(node, 1)
        # self.assertEqual(node_to_list(swapped), [64, 46, 66, 35, 80])
        # node = list_to_node([80])
        # swapped = self.s.swapNodes(node, 1)
        # self.assertEqual(node_to_list(swapped), [80])
        # node = list_to_node([1, 2, 3, 4, 5, 6, 7])
        # swapped = self.s.swapNodes(node, 6)
        # self.assertEqual(node_to_list(swapped), [1, 6, 3, 4, 5, 2, 7])


if __name__ == "__main__":
    main()
