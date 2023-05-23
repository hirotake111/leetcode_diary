"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/
703. Kth Largest Element in a Stream

Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
"""
from typing import List
from heapq import heappush, heappop


class KthLargest:
    """
    Priority queue approach
    We just need top k largest elements and can get rid of the rest.
    """

    k: int
    nums: List[int]

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = []
        for n in nums:
            self.add(n)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heappush(self.nums, val)
        elif self.nums[0] < val:
            # Pop the smallest and push a new one
            heappop(self.nums)
            heappush(self.nums, val)
        return self.nums[0]

    """Binary search approach"""
    # def __init__(self, k: int, nums: List[int]):
    #    self.nums = sorted(nums)
    #    self.k = k
    #
    #
    # def add(self, val: int) -> int:
    #    """Binary search approach"""
    #    #i = bisect.bisect(self.nums, val)
    #    #self.nums = self.nums[:i] + [val] + self.nums[i:]
    #    #return self.nums[-self.k]
