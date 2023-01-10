from typing import List


class MedianFinder:
    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        if self.arr == []:
            self.arr = [num]
            return

        low, high = 0, len(self.arr) - 1

        if num <= self.arr[low]:
            self.arr.insert(0, num)
            return
        if self.arr[high] <= num:
            self.arr += [num]
            return

        while low + 1 < high:
            mid = (high - low) // 2
            if self.arr[mid] == num:
                self.arr.insert(mid, num)
                return
            if self.arr[mid] < num:
                low = mid
            else:
                high = mid
        self.arr.insert(high, num)

    def findMedian(self) -> float:
        mid = len(self.arr) // 2
        if len(self.arr) % 2:
            # odd
            return float(self.arr[mid])
        # even
        return (self.arr[mid - 1] + self.arr[mid]) / 2


if __name__ == "__main__":
    finder = MedianFinder()
    finder.addNum(10)
    finder.addNum(20)
    finder.addNum(5)
    finder.addNum(15)
    print(finder.arr)

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
