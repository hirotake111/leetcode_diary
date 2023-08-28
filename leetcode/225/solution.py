"""
https://leetcode.com/problems/implement-stack-using-queues/
225. Implement Stack using Queues
"""
from collections import deque


class MyStack:
    def __init__(self):
        self.p, self.s = deque(), deque()

    def push(self, x: int) -> None:
        self.p, self.s = self.s, self.p
        self.p.append(x)
        while self.s:
            self.p.append(self.s.popleft())

    def pop(self) -> int:
        return self.p.popleft()

    def top(self) -> int:
        return self.p[0]

    def empty(self) -> bool:
        return len(self.p) == 0
