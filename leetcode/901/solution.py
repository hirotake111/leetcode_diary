from typing import List, Tuple
from unittest import TestCase, main


class StockSpanner:
    def __init__(self):
        self.prev_price = 100001
        self.prev_cout = 0

    def next(self, price: int) -> int:
        if price < self.prev_price:
            self.prev_cout = 1
            return 1
        self.prev_cout += 1


class Test(TestCase):
    data_set: List[Tuple[int, int]] = [
        (100, 1),
        (80, 1),
        (60, 1),
        (70, 2),
        (60, 1),
        (75, 4),
        (85, 6),
    ]

    def test_solution(self):
        stockSpanner = StockSpanner()
        for given, expected in self.data_set:
            self.assertEqual((given, stockSpanner.next(given)), (given, expected))


if __name__ == "__main__":
    main()
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
