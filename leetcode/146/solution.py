"""
https://leetcode.com/problems/lru-cache/description/
146. LRU Cache
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:

LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
int get(int key) Return the value of the key if the key exists, otherwise return -1.
void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
The functions get and put must each run in O(1) average time complexity.
"""
from typing import Dict


class DoublyLinkedList:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.bwd = None
        self.fwd = None


class LRUCache:
    capacity: int
    cache: Dict[int, DoublyLinkedList]
    head: DoublyLinkedList
    tail: DoublyLinkedList

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.counts = 0
        self.cache = {}
        self.head = DoublyLinkedList(0, -1)
        self.tail = DoublyLinkedList(0, -1)
        self.connect(self.head, self.tail)

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        dll = self.cache[key]
        self.update(dll)
        return dll.val

    def put(self, key: int, value: int) -> None:
        dll = DoublyLinkedList(key, value)
        if key in self.cache:
            old_one = self.cache[key]
            self.remove_from_list(old_one)
            self.push_tail(dll)
            return
        # Add a new key
        self.push_tail(dll)
        self.counts += 1
        if self.capacity < self.counts:
            self.pop_oldest()

    def connect(self, older: DoublyLinkedList, newer: DoublyLinkedList):
        older.bwd = newer
        newer.fwd = older

    def push_tail(self, dll: DoublyLinkedList):
        old_one = self.tail.fwd
        self.connect(old_one, dll)
        self.connect(dll, self.tail)
        self.cache[dll.key] = dll

    def pop_oldest(self):
        to_be_removed = self.head.bwd
        self.remove_from_list(to_be_removed)

    def remove_from_list(self, to_be_removed: DoublyLinkedList):
        fwd, bwd = to_be_removed.fwd, to_be_removed.bwd
        self.connect(fwd, bwd)
        to_be_removed.fwd = None
        to_be_removed.bwd = None
        del self.cache[to_be_removed.key]

    def update(self, dll: DoublyLinkedList):
        self.remove_from_list(dll)
        self.push_tail(dll)
