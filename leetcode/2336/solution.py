"""
https://leetcode.com/problems/smallest-number-in-infinite-set/
2336. Smallest Number in Infinite Set

You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
"""
from heapq import heapify, heappop, heappush


class SmallestInfiniteSet:
    def __init__(self):
        self.heap = [i for i in range(1, 1001)]
        self.set = set(self.heap)
        heapify(self.heap)

    def popSmallest(self) -> int:
        n = heappop(self.heap)
        self.set.remove(n)
        return n

    def addBack(self, num: int) -> None:
        if num not in self.set:
            self.set.add(num)
            heappush(self.heap, num)
