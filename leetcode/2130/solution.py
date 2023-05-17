"""
https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/description/
2130. Maximum Twin Sum of a Linked List

In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.
The twin sum is defined as the sum of a node and its twin.

Given the head of a linked list with even length, return the maximum twin sum of the linked list.


"""
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr, answer = [], 0
        while head:
            arr.append(head.val)
            head = head.next

        i, j = 0, len(arr) - 1
        while i < j:
            answer = max(answer, arr[i] + arr[j])
            i, j = i + 1, j - 1

        return answer
