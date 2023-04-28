"""
https://leetcode.com/problems/similar-string-groups/
839. Similar String Groups

Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?
"""
from typing import List, Callable


class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        """Union & Find approach"""
        n = len(strs)
        uf = UnionFind(strs, matches)
        for i in range(0, n - 1):
            for j in range(1, n):
                uf.perform(i, j)

        return uf.get_size()


def matches(s1: str, s2: str) -> bool:
    """Compares two strings and return True if two are the same or similar"""
    diff = 0
    if s1 == s2:
        return True
    for c1, c2 in zip(s1, s2):
        if c1 != c2:
            if diff >= 2:
                # Too many difference between two strings
                return False
            diff += 1
    return diff == 2


class UnionFind:
    def __init__(self, strs: List[str], compare: Callable[[str, str], bool]):
        self.strs = strs
        self.compare = compare
        self.roots = [i for i in range(len(strs))]

    def find(self, idx: int) -> int:
        """Returns the root value of idx"""
        if self.roots[idx] != idx:
            self.roots[idx] = self.find(self.roots[idx])
        return self.roots[idx]

    def union(self, i: int, j: int):
        """Updates root value of either i or j"""
        root_i, root_j = self.find(i), self.find(j)
        if root_i > root_j:
            root_i, root_j = root_j, root_i
        self.roots[root_j] = root_i

    def perform(self, i: int, j: int):
        """Performs the combination of compare and union"""
        if self.compare(self.strs[i], self.strs[j]):
            # The two words are similar (and will be in the same group)
            self.union(i, j)

    def get_size(self) -> int:
        """Returns the number of unique numbers in self.roots"""
        s = set()
        for root in self.roots:
            s.add(self.find(root))
        return len(s)
