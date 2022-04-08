import re
from typing import List, Optional, cast
from unittest import main, TestCase

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        divide and conquer approach
        """
        # assuming inputs have been already divided
        def merge_nodes(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
            l = len(lists)
            if l == 0:
                return None
            if l == 1:
                return lists[0]

            return merge_nodes(
                [
                    merge_two_nodes(lists[i], lists[i + 1] if i + 1 < l else None)
                    for i in range(0, l, 2)
                ]
            )

        def merge_two_nodes(
            x: Optional[ListNode], y: Optional[ListNode]
        ) -> Optional[ListNode]:
            if x is None:
                return y
            if y is None:
                return x

            head = None
            prev = None

            while True:
                if x is y is None:
                    break
                elif x is None:
                    node = y
                    y = y.next
                elif y is None:
                    node = x
                    x = x.next
                elif x.val > y.val:
                    node = y
                    y = y.next
                else:
                    node = x
                    x = x.next
                if head is None:
                    head = node
                if prev:
                    prev.next = node
                prev = node

            return head

        return merge_nodes(lists)
        """
        Compare one by one approach
        """
        # head, prev = None, None

        # while True:
        #     min_idx = 10001  # 10^4+1

        #     # find minimum value among lists
        #     for i in range(len(lists)):
        #         if lists[i] and (min_idx == 10001 or lists[i].val < lists[min_idx].val):
        #             min_idx = i

        #     # if min_idx is 10^4+1, it means there is no lists anymore -> exist loop
        #     if min_idx == 10001:
        #         break
        #     # add it to node
        #     node = lists[min_idx]
        #     if head is None:
        #         head = node
        #     if prev:
        #         prev.next = node
        #     prev = node
        #     lists[min_idx] = node.next

        # return head


def list_to_node(l: List[int]) -> Optional[ListNode]:
    head = None
    prev = None

    for val in l:
        node = ListNode(val=val)
        if head is None:
            head = node
        if prev:
            prev.next = node
        prev = node

    return head


def node_to_list(node: ListNode) -> List[int]:
    ans: List[int] = []
    while node:
        ans.append(node.val)
        node = node.next
    return ans


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        # l = [1, 2, 3, 4, 5]
        # self.assertEqual(node_to_list(list_to_node(l)), l)
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        nodes = [list_to_node(l) for l in lists]
        expected = [1, 1, 2, 3, 4, 4, 5, 6]
        merged = self.s.mergeKLists(nodes)
        self.assertEqual(node_to_list(merged), expected)


if __name__ == "__main__":
    main()
