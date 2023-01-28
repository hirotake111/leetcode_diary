"""
https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
352. Data Stream as Disjoint Intervals
Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:

SummaryRanges() Initializes the object with an empty stream.
void addNum(int value) Adds the integer value to the stream.
int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.
"""
from typing import List, Optional
from heapq import heappush, heappop


class SummaryRanges:
    arr: List[int]

    def __init__(self):
        self.arr = []

    def addNum(self, value: int) -> None:
        if len(self.arr) == 0:
            self.arr = [value]
            return

        low, high = 0, len(self.arr) - 1
        if self.arr[high] <= value:
            if self.arr[high] < value:
                self.arr.append(value)
            return
        elif value <= self.arr[low]:
            if value < self.arr[low]:
                self.arr.insert(0, value)
            return

        while True:
            mid = (high - low) // 2 + low
            if value == self.arr[mid]:
                return

            elif value < self.arr[mid]:
                if low + 1 == mid:
                    break
                high = mid
                continue

            if mid + 1 == high:
                mid += 1
                break
            low = mid

        self.arr.insert(mid, value)

    def getIntervals(self) -> List[List[int]]:
        prev: Optional[int] = None
        answer: List[List[int]] = []
        for value in self.arr:
            if prev is None:
                cur = [value, value]
            elif value - 1 == prev:
                cur[1] = value
            else:
                answer.append(cur)
                cur = [value, value]
            prev = value

        answer.append(cur)
        return answer
