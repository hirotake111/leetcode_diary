from unittest import main, TestCase
from typing import Optional, List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pass


def get_node(arr: List[int]) -> ListNode:
    head = ListNode()
    node = head
    for val in arr:
        node.val = val


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        self.assertEqual(self.s.removeNthFromEnd(head=[1, 2, 3, 4, 5], n=2), 2)
