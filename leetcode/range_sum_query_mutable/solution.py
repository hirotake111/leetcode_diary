from typing import List
from math import ceil, log2
from unittest import TestCase, main


class NumArray:
    """segment tree approach"""

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.length = len(nums)
        level = int(ceil(log2(self.length)))
        self.max_size = (2 ** (level + 1)) - 1
        self.tree = [0] * self.max_size

        def build(idx: int, begin: int, end: int) -> int:
            if begin == end:
                self.tree[idx] = self.nums[begin]
                return self.nums[begin]
            mid = self.__get_mid(begin, end)
            left = build(2 * idx + 1, begin, mid)
            right = build(2 * idx + 2, mid + 1, end)
            self.tree[idx] = left + right
            return self.tree[idx]

        build(0, 0, self.length - 1)

    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val

        def update_tree(tree_idx: int, begin: int, end: int) -> None:
            if self.max_size <= tree_idx:
                return
            if index < begin or end < index:
                return
            if begin <= index <= end:
                self.tree[tree_idx] += diff
            if begin == end:
                return
            mid = self.__get_mid(begin, end)
            update_tree(tree_idx * 2 + 1, begin, mid)
            update_tree(tree_idx * 2 + 2, mid + 1, end)

        update_tree(0, 0, self.length - 1)

    def sumRange(self, left: int, right: int) -> int:
        def calc_range(index: int, begin: int, end: int) -> int:
            if left <= begin and end <= right:
                return self.tree[index]
            if end < left or right < begin:
                return 0
            mid = self.__get_mid(begin, end)
            left_nodes = calc_range(index * 2 + 1, begin, mid)
            right_nodes = calc_range(index * 2 + 2, mid + 1, end)
            return left_nodes + right_nodes

        return calc_range(0, 0, self.length - 1)

    def __get_mid(self, begin: int, end: int) -> int:
        return begin + (end - begin) // 2

    def __build_tree(self, idx: int, begin: int, end: int) -> int:
        if begin == end:
            self.tree[idx] = self.nums[begin]
            return self.nums[begin]
        mid = self.__get_mid(begin, end)
        left = self.__build_tree(2 * idx + 1, begin, mid)
        right = self.__build_tree(2 * idx + 2, mid + 1, end)
        self.tree[idx] = left + right
        return self.tree[idx]

    def show(self) -> List[int]:
        return self.nums
        # arr: List[int] = [0] * self.length

        # def get_node(tree_index: int, begin: int, end: int):
        # if begin == end:
        # arr[begin] = self.tree[tree_index]
        # return
        # mid = self.get_mid(begin, end)
        # get_node(tree_index * 2 + 1, begin, mid)
        # get_node(tree_index * 2 + 2, mid + 1, end)

        # get_node(0, 0, self.length - 1)
        # return arr


class Test(TestCase):
    def test_solution(self):
        arr = NumArray([0, 9, 5, 7, 3])
        arr.update(4, 5)
        self.assertEqual(arr.show(), [0, 9, 5, 7, 5])
        arr = NumArray([1, 3, 5])
        self.assertEqual(arr.sumRange(0, 2), 9)
        self.assertEqual(arr.sumRange(1, 2), 8)
        arr.update(1, 10)
        self.assertEqual(arr.show(), [1, 10, 5])
        arr.update(1, 4)
        self.assertEqual(arr.show(), [1, 4, 5])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)

if __name__ == "__main__":
    main()
