"""
https://leetcode.com/problems/snapshot-array/
1146. Snapshot Array

Implement a SnapshotArray that supports the following interface:

SnapshotArray(int length) initializes an array-like data structure with the given length. Initially, each element equals 0.
void set(index, val) sets the element at the given index to be equal to val.
int snap() takes a snapshot of the array and returns the snap_id: the total number of times we called snap() minus 1.
int get(index, snap_id) returns the value at the given index, at the time we took the snapshot with the given snap_id
"""
from typing import List
import bisect

"""Binary Search approach"""


class SnapshotArray:
    values: List[List[int]]
    ids: List[List[int]]
    current: int

    def __init__(self, length: int):
        self.values = [[0] for _ in range(length)]
        self.ids = [[0] for _ in range(length)]
        self.current = 0

    def set(self, index: int, val: int) -> None:
        # Update or insert new one
        if self.ids[index][-1] == self.current:
            self.values[index][-1] = val
        else:
            self.ids[index].append(self.current)
            self.values[index].append(val)

    def snap(self) -> int:
        self.current += 1
        return self.current - 1

    def get(self, index: int, snap_id: int) -> int:
        values = self.values[index]
        ids = self.ids[index]
        # Shortcuts
        if snap_id == 0:
            return values[0]
        if ids[-1] <= snap_id:
            return values[-1]
        idx = bisect.bisect_right(ids, snap_id)
        # idx now points to an insertion point.
        # Therefore, we need to subtract 1 from the idx
        return values[idx - 1]


# # Linked List approach (TLE)
# class LinkedList:
# snap_id: int
# value: int
# next: Optional["LinkedList"]

# def __init__(self, snap_id: int, val: int):
# self.snap_id = snap_id
# self.val = val
# self.next = None

# def __str__(self):
# return f"{self.snap_id}, {self.val}"


# class SnapshotArray:
# l: List[LinkedList]
# snap_id: int

# def __init__(self, length: int):
# self.l = [LinkedList(0, 0) for _ in range(length)]
# self.snap_id = 0

# def set(self, index: int, val: int) -> None:
# node = self.l[index]
# # Search the latest node
# while node.next:
# node = node.next
# if node.snap_id == self.snap_id:
# # Simply update the value of the node
# node.val = val
# else:
# # Create a new node
# node.next = LinkedList(self.snap_id, val)

# def snap(self) -> int:
# snap_id = self.snap_id
# self.snap_id += 1
# return snap_id

# def get(self, index: int, snap_id: int) -> int:
# node = self.l[index]
# if node.snap_id == snap_id:
# return node.val
# prev = node
# next_node = node.next
# while next_node:
# if next_node.snap_id > snap_id:
# break
# prev = next_node
# next_node = node.next
# return prev.val


# # 2D array approach (TLE)
# class SnapshotArray:
# l: List[List[int]]
# current: int

# def __init__(self, length: int):
# self.l = []
# self.l.append([0] * length)
# self.current = 0

# def set(self, index: int, val: int) -> None:
# self.l[self.current][index] = val

# def snap(self) -> int:
# snap_id = self.current
# self.l.append(self.l[snap_id].copy())
# self.current += 1
# return snap_id

# def get(self, index: int, snap_id: int) -> int:
# return self.l[snap_id][index]


# Your SnapshotArray object will be instantiated and called as such:
# obj = SnapshotArray(length)
# obj.set(index,val)
# param_2 = obj.snap()
# param_3 = obj.get(index,snap_id)
