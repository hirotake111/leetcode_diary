from typing import List
from unittest import TestCase, main


class MyHashSet:
    def __init__(self):
        self._data: List[int] = []

    def add(self, key: int) -> None:
        if not self.contains(key):
            self._data.append(key)

    def remove(self, key: int) -> None:
        if self.contains(key):
            idx = self._data.index(key)
            self._data = self._data[:idx] + self._data[idx + 1 :]

    def contains(self, key: int) -> bool:
        return key in self._data


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)


class TestSolution(TestCase):
    def test_solution(self):
        hs = MyHashSet()
        hs.add(1)
        hs.add(2)
        self.assertEqual(hs.contains(1), True)
        self.assertEqual(hs.contains(3), False)
        hs.add(2)
        self.assertEqual(hs.contains(2), True)
        hs.remove(2)
        self.assertEqual(hs.contains(2), False)


if __name__ == "__main__":
    main()
