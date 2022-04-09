import heapq
import tarfile
from unittest import main, TestCase
from typing import Any, List, Optional


class KthLargest:
    k: int
    heap: List[int]
    length: int

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = sorted(nums)
        length = len(nums)
        if length > k:
            self.heap = self.heap[length - k :]

    def add(self, val: int) -> Optional[int]:
        if len(self.heap) < self.k:
            # self.nums has less than k elements -> add val
            heapq.heappush(self.heap, val)
            return self.heap[0]

        # self.num has k elements
        elif self.heap[0] < val:
            # val is larger than self.nums[0] -> add it to the array
            heapq.heapreplace(self.heap, val)
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

"""
[4,5,8] 4
[4,5,8] 4
[5,5,8] 5
[5,8,10] 5
[8,9,10] 8
"""


class TestSolution(TestCase):
    def func(self, data: Any, expected: List[int]):
        obj = KthLargest(data[0][0], data[0][1])
        for i, j in zip(data[1:], expected):
            self.assertEqual(obj.add(i[0]), j)

    def test_solution(self):
        data = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
        expected = [4, 5, 5, 8, 8]
        self.func(data, expected)

        data = [[1, []], [-3], [-2], [-4], [0], [4]]
        expected = [-3, -2, -2, 0, 4]
        self.func(data, expected)
        data = [[3, [5, -1]], [2], [1], [-1], [3], [4]]
        expected = [-1, 1, 1, 2, 3]
        self.func(data, expected)


if __name__ == "__main__":
    main()
