"""
https://leetcode.com/problems/design-hashset/
705. Design HashSet

Design a HashSet without using any built-in hash table libraries.

Implement MyHashSet class:

void add(key) Inserts the value key into the HashSet.
bool contains(key) Returns whether the value key exists in the HashSet or not.
void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
"""
from typing import List

INITIAL_CAPACITY = 1024


class MyHashSet:
    store: List[bool]

    def __init__(self):
        self.capacity = INITIAL_CAPACITY
        self.store = [False] * self.capacity

    def add(self, key: int) -> None:
        # Dynamically add extra elements if self.capacity is not enough
        if self.capacity <= key:
            new_capacity = key + 1
            self.store += [False] * (new_capacity - self.capacity)
            self.capacity = new_capacity
        self.store[key] = True

    def remove(self, key: int) -> None:
        if self.capacity <= key:
            return
        self.store[key] = False

    def contains(self, key: int) -> bool:
        if self.capacity <= key:
            return False
        return self.store[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
