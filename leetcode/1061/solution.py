"""
https://leetcode.com/problems/lexicographically-smallest-equivalent-string/
1061. Lexicographically Smallest Equivalent String

You are given two strings of the same length s1 and s2 and a string baseStr.

We say s1[i] and s2[i] are equivalent characters.

For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
Equivalent characters follow the usual rules of any equivalence relation:

Reflexivity: 'a' == 'a'.
Symmetry: 'a' == 'b' implies 'b' == 'a'.
Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
For example, given the equivalency information from s1 = "abc" and s2 = "cde", "acd" and "aab" are equivalent strings of baseStr = "eed", and "aab" is the lexicographically smallest equivalent string of baseStr.

Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.
"""
from typing import Tuple, List
from unittest import TestCase, main


class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        uf = UnionFind(s1, s2)
        return uf.get_equivalent_string(baseStr)


class UnionFind:
    __tree: List[int]

    def __init__(self, s1: str, s2: str) -> None:
        # Create a list [0..26], with length of a to z.
        # each element's value (root) is index,
        # indicating each root points the character itself
        self.__tree = [i for i in range(26)]
        self.__union(s1, s2)

    def get_equivalent_string(self, s: str) -> str:
        result = [c for c in s]
        for i, c in enumerate(result):
            # Get root index of c
            root = self.__find(self.__encode(c))
            # Decode it when ita gets stored in result
            result[i] = self.__decode(root)

        return "".join(result)

    def __union(self, s1: str, s2: str):
        for c1, c2 in zip(s1, s2):
            if c1 == c2:  # Do noting with the same characters
                continue
            # Find the root of a and b in the first place
            root_1 = self.__find(self.__encode(c1))
            root_2 = self.__find(self.__encode(c2))
            # convert and swap (0: smaller index, 1: greater index)
            smaller, greater = self.__swap(root_1, root_2)
            # tree[greater] should be value smaller
            self.__set(greater, smaller)

    def __find(self, idx: int) -> int:
        if self.__tree[idx] == idx:
            return idx
        # Recursively find and set root
        root = self.__find(self.__tree[idx])
        self.__tree[idx] = root
        return root

    def __set(self, idx: int, value: int):
        self.__tree[idx] = value

    def __swap(self, a: int, b: int) -> Tuple[int, int]:
        if b < a:
            return b, a
        return a, b

    def __encode(self, s: str) -> int:
        return ord(s) - 97

    def __decode(self, n: int) -> str:
        return chr(n + 97)


class Test(TestCase):
    data: List[Tuple[str, str, str, str]] = [
        ("parker", "morris", "parser", "makkek"),
    ]

    def test_solution(self):
        s = Solution()
        for a, b, c, d in self.data:
            self.assertEqual(s.smallestEquivalentString(a, b, c), d)


if __name__ == "__main__":
    main()
