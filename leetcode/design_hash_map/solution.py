from typing import List, Optional
from unittest import main, TestCase


class Node:
    kye: int
    value: int
    next: Optional["Node"]

    def __init__(self, key=-1, value=-1, next=None) -> None:
        self.key = key
        self.value = value
        self.next = None


class MyHashMap:
    def __init__(self):
        self.n = 128
        self._arr: List[Optional["Node"]] = [None] * self.n

    def put(self, key: int, value: int) -> None:
        new_key = key % self.n
        node = self._arr[new_key]
        if node is None:
            self._arr[new_key] = Node(key, value)
            return
        while node:
            if node.key == key:
                # update value
                node.value = value
                return
            if node.next is None:
                node.next = Node(key, value)
                return
            node = node.next

    def get(self, key: int) -> int:
        new_key = key % self.n
        node = self._arr[new_key]
        while node:
            if node.key == key:
                return node.value
            node = node.next
        return -1

    def remove(self, key: int) -> None:
        new_key = key % self.n
        node = self._arr[new_key]
        prev: Optional["Node"] = None
        while node:
            if node.key == key:
                # remove node
                if prev is not None:
                    # prev -> next
                    prev.next = node.next
                    return
                else:
                    # next should be first node
                    self._arr[new_key] = node.next
                    return
            prev = node
            node = node.next


class TestSolution(TestCase):
    def test_solution(self):
        hm = MyHashMap()
        hm.put(1, 1)
        hm.put(2, 2)
        self.assertEqual(hm.get(1), 1)
        self.assertEqual(hm.get(3), -1)
        hm.put(2, 1)
        self.assertEqual(hm.get(2), 1)
        hm.remove(2)
        self.assertEqual(hm.get(2), -1)
        hm.put(970, 538)


if __name__ == "__main__":
    main()
