from typing import cast
from unittest import main, TestCase
from queue import Queue


class MyStack:
    q1: Queue[int]
    q2: Queue[int]

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        self.q1.put(x)

    def pop(self) -> int:
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get(block=False))
        result = self.q1.get(block=False)
        self.q1, self.q2 = self.q2, self.q1
        return result

    def top(self) -> int:
        result = self.pop()
        self.q1.put(result)
        return result

    def empty(self) -> bool:
        return self.q1.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


class TestSolution(TestCase):
    def test_solution(self):
        stack = MyStack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.top(), 2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.empty(), False)


if __name__ == "__main__":
    main()
