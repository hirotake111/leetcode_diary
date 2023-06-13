"""
https://leetcode.com/problems/equal-row-and-column-pairs/
2352. Equal Row and Column Pairs

Given a 0-indexed n x n integer matrix grid, return the number of pairs (ri, cj) such that row ri and column cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e., an equal array).
"""
from typing import Dict, List


class Trie:
    counts: int
    children: Dict[int, "Trie"]

    def __init__(self):
        self.counts = 1
        self.children = {}


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        """Hash Map approach"""
        # n = len(grid)
        # hm = defaultdict(int)
        # for col in range(n):
        #    hm[tuple(grid[row][col] for row in range(n))] += 1
        # return sum([hm[tuple(row)] for row in grid])
        """Trie approach"""
        n = len(grid)
        root = Trie()
        # Read through each column and create a trie
        for col in range(n):
            trie = root
            for row in range(n):
                x = grid[row][col]
                if x in trie.children:
                    trie.children[x].counts += 1
                else:
                    trie.children[x] = Trie()
                trie = trie.children[x]

        # Search each row
        answer = 0
        for line in grid:
            trie = root
            matches = True
            for v in line:
                if v not in trie.children:
                    matches = False
                    break
                trie = trie.children[v]
            if matches:
                # Found the same row
                answer += trie.counts
        return answer
