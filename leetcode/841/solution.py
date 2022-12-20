"""
841. Keys and Rooms
https://leetcode.com/problems/keys-and-rooms/
"""
from typing import List, Set
from queue import Queue


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        """DFS approach"""
        locked: Set[int] = set(range(1, len(rooms)))

        def dfs(room: int):
            for key in rooms[room]:
                if key not in locked:
                    continue
                # we have a key
                # Unlock it first
                locked.remove(key)
                # And then go to the next
                dfs(key)

        dfs(0)
        return len(locked) == 0

        # """BFS approach"""
        # n = len(rooms)
        # locked: Set[int] = set(range(1, n))
        # queue: Queue[int] = Queue()
        # # Push the first key (0)
        # queue.put(0)
        # while not queue.empty():
        # room = queue.get()
        # # Pick up each key in the room
        # for key in rooms[room]:
        # # If key is in locked, put the key in the queue
        # # and then unlock it
        # if key in locked:
        # queue.put(key)
        # locked.remove(key)

        # return len(locked) == 0
