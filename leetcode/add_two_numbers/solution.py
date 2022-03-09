from typing import List, Optional
from unittest import TestCase,main

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        li1 = node_to_list(l1)
        li2 = node_to_list(l2)
        length = max(len(li1), len(li2))
        li1 += (length - len(li1)) * [0]
        li2 += (length - len(li2)) * [0]
        result = length * [0]
        for i in range(length):
            c, v = divmod(li1[i] + li2[i], 10)
            result[i] = v + carry 
            carry = c
        return list_to_node(result)
        # result = ListNode()
        # node = result
        # carry = 0

        # while True:
        #     c, v = divmod(l1.val or 0 + l2.val or 0, 10)
        #     node.val = v +carry
        #     carry = c
        #     if l1.next is None or l2.next is None:
        #         break
        #     l1 = l1.next
        #     l2 = l2.next
        #     node.next = ListNode()
        #     node = node.next

        # return result


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

def node_to_list(l:ListNode):
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
        node = list_to_node([1,2,3])
        self.assertEqual(node_to_list( node), [1,2,3])

    # def test_input(self):
    #     l1 = list_to_node([2,4,3])
    #     l2 = list_to_node([5,6,4])
    #     node = self.s.addTwoNumbers(l1, l2)
    #     self.assertEqual(node_to_list(node), [7,0,8])
    
    def test_input2(self):
        l1 = list_to_node([9,9,9,9,9,9,9])
        l2 = list_to_node([9,9,9,9])
        node = self.s.addTwoNumbers(l1, l2)
        self.assertEqual(node_to_list(node), [7,0,8])



if __name__ == "__main__":
    main()