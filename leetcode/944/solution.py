"""
https://leetcode.com/problems/delete-columns-to-make-sorted/
944. Delete Columns to Make Sorted

You are given an array of n strings strs, all of the same length.

The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:

- abc
- bce
- cae
You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        len_row, len_col = len(strs), len(strs[0])
        columns = [0] * len_col
        # If we have only 1 string, return 1
        if len_row == 1:
            return 1

        for row in range(1, len_row):
            prev_row = strs[row - 1]
            curr_row = strs[row]
            for col in range(len_col):
                # If the colum has been already evaluated as not sorted, skip it
                if columns[col] == 1:
                    continue
                # Check to see if current ch is larger than or equal to previous one
                if ord(curr_row[col]) < ord(prev_row[col]):
                    columns[col] == 1

        return sum(columns)


class Test(TestCase):
    data: List[Tuple[List[str], int]] = [
        (["cba", "daf", "ghi"], 1),
    ]

    def test_solution(self):
        s = Solution()
        for input, expected in self.data:
            self.assertEqual(s.minDeletionSize(input), expected)


if __name__ == "__main__":
    main()
