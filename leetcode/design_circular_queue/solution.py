from typing import List


class MyCircularQueue:
    k: int
    begin: int
    end: int
    queue: List[int]

    def __init__(self, k: int):
        self.k = k
        self.begin = 0
        self.end = -1
        self.queue = [0] * k

    def enQueue(self, value: int) -> bool:
        """Inserts an element into the circular queue. Return true if the operation is successful."""
        if self.isFull():
            return False
        if self.end == -1:
            self.end = self.begin
        else:
            self.end = (self.end + 1) % self.k
        self.queue[self.end] = value
        return True

    def deQueue(self) -> bool:
        """Deletes an element from the circular queue. Return true if the operation is successful."""
        if self.isEmpty():
            return False
        if self.begin == self.end:
            # the queue has only one value in it -> set self.end to -1
            self.end = -1
            return True
        self.begin = (self.begin + 1) % self.k
        return True

    def Front(self) -> int:
        """Gets the front item from the queue. If queue is empty, return -1."""
        if self.isEmpty():
            return -1
        return self.queue[self.begin]

    def Rear(self) -> int:
        """Gets the last item from the queue. If the queue is empty, return -1."""
        if self.isEmpty():
            return -1
        return self.queue[self.end]

    def isEmpty(self) -> bool:
        """Checks whether the circular queue is empty or not."""
        return self.end == -1

    def isFull(self) -> bool:
        """Checks whether the circular queue is full or not."""
        if self.end == -1:
            return False
        next = (self.end + 1) % self.k
        return next == self.begin


if __name__ == "__main__":
    ring = MyCircularQueue(2)
    assert ring.enQueue(4) == True
    assert ring.Rear() == 4
    assert ring.enQueue(9) == True
    assert ring.deQueue() == True
    assert ring.Front() == 9
    assert ring.deQueue() == True
    assert ring.deQueue() == False
    assert ring.isEmpty() == True
    assert ring.deQueue() == False
    assert ring.enQueue(6) == True
    assert ring.enQueue(4) == True


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
