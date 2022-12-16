"""
232. Implement Queue using Stacks
https://leetcode.com/problems/implement-queue-using-stacks/
"""
from typing import List


class MyQueue:
    def __init__(self):
        self.stack = []
        self.top = self.bottom = -1

    def push(self, x: int) -> None:
        if self.empty():
            # no elements in it -> push a new item and init index
            self.stack.append(x)
            self.top = self.bottom = 0
            return
        # we have had more than 0 -> increment self.top
        self.stack.append(x)
        self.top += 1

    def pop(self) -> int:
        v = self.peek()
        if self.top == self.bottom:
            # we had only one element in it
            # -> empty the stack
            self.stack = []
            self.top = self.bottom = -1
            return v

        # we had some elements -> increment bottom
        self.bottom += 1
        return v

    def peek(self) -> int:
        return self.stack[self.bottom]

    def empty(self) -> bool:
        return self.stack == []


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
