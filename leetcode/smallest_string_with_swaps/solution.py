from unittest import TestCase, main
from typing import DefaultDict, Dict, List


class UnionFind:
    def __init__(self, n: int) -> None:
        self.parent = [i for i in range(n)]

    def find(self, n: int):
        if self.parent[n] == n:
            # this is a root of a graph
            return n
        self.parent[n] = self.find(self.parent[n])
        return self.parent[n]

    def union(self, a: int, b: int) -> None:
        self.parent[self.find(a)] = self.find(b)


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # generate a graph
        uf = UnionFind(len(s))
        for x, y in pairs:
            uf.union(x, y)

        # divide strings into groups
        tmp: Dict[int, str] = DefaultDict(str)
        for i, ch in enumerate(s):
            group_id = uf.find(i)
            uf.parent[i] = group_id
            tmp[uf.find(i)] += ch
        # sort strings within a graph
        for k, v in tmp.items():
            tmp[k] = "".join(sorted(v))

        # conbine those strings
        ans = ""
        for i, _ in enumerate(s):
            group_id = uf.parent[i]
            ans += tmp[group_id][0]
            tmp[group_id] = tmp[group_id][1:]
        return ans


class TestSolution(TestCase):
    s = Solution()

    def test_solutio(self):
        # s = "dcab"
        # pairs = [[0, 3], [1, 2]]
        # self.assertEqual(self.s.smallestStringWithSwaps(s, pairs), "bacd")
        s = "dcab"
        pairs = [[0, 3], [1, 2], [0, 2]]
        self.assertEqual(self.s.smallestStringWithSwaps(s, pairs), "abcd")
        # s = "cba"
        # pairs = [[0, 1], [1, 2]]
        # self.assertEqual(self.s.smallestStringWithSwaps(s, pairs), "abc")


if __name__ == "__main__":
    main()
