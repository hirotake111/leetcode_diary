from unittest import TestCase, main
from typing import List


class Iterator:
    def __init__(self, nums):
        self.nums = nums
        self.idx = -1
        self.last_index = len(nums) - 1

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """
        return self.idx < self.last_index

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """
        self.idx += 1
        return self.nums[self.idx]


class PeekingIterator:
    iter: Iterator
    idx: int
    length: int
    _nextValue: int

    def __init__(self, iterator: Iterator):
        self.iter = iterator
        self._hasNext = iterator.hasNext()
        if self._hasNext:
            self._nextValue = iterator.next()

    def peek(self) -> int:
        return self._nextValue

    def next(self) -> int:
        next_value = self._nextValue
        self._hasNext = self.iter.hasNext()
        if self._hasNext:
            self._nextValue = self.iter.next()
        return next_value

    def hasNext(self) -> bool:
        return self._hasNext


# Your PeekingIterator object will be instantiated and called as such:
# iter = PeekingIterator(Iterator(nums))
# while iter.hasNext():
#     val = iter.peek()   # Get the next element but not advance the iterator.
#     iter.next()         # Should return the same value as [val].


class TestSolution(TestCase):
    def test_solution(self):
        peekingIterator = PeekingIterator(Iterator([1, 2, 3]))  # [1,2,3]
        self.assertEqual(
            peekingIterator.next(), 1
        )  # return 1, the pointer moves to the next element [1,2,3].
        self.assertEqual(
            peekingIterator.peek(), 2
        )  # return 2, the pointer does not move [1,2,3].
        self.assertEqual(
            peekingIterator.next(), 2
        )  # return 2, the pointer moves to the next element [1,2,3]
        self.assertEqual(
            peekingIterator.next(), 3
        )  # return 3, the pointer moves to the next element [1,2,3]
        self.assertEqual(peekingIterator.hasNext(), False)  # return False


if __name__ == "__main__":
    main()
