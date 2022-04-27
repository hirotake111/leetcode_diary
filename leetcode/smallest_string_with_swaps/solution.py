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
        return self.find(self.parent[n])

    def union(self, a: int, b: int) -> bool:
        pa, pb = self.find(a), self.find(b)
        if pa == pb:
            # they are already in the same group -> return False
            return False
        # they are not in the same group -> combine and return True
        self.parent[pa] = pb
        return True


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        # generate a graph
        uf = UnionFind(len(s))
        l = len(s)
        for x, y in pairs:
            uf.union(x, y)

        # divide strings into groups
        tmp: Dict[int, str] = DefaultDict(str)
        groups: List[int] = [-1] * l
        for i in range(l):
            group_id = uf.find(i)
            tmp[group_id] += s[i]
            groups[i] = group_id
        # sort strings within a graph
        for k, v in tmp.items():
            tmp[k] = "".join(sorted(v))

        # conbine those strings
        ans = ""
        for i in range(l):
            group_id = groups[i]
            ans += tmp[group_id][0]
            tmp[group_id] = tmp[group_id][1:]
        return ans


class TestSolution(TestCase):
    s = Solution()

    def test_solutio(self):
        s = "dcab"
        pairs = [[0, 3], [1, 2]]
        self.assertEqual(self.s.smallestStringWithSwaps(s, pairs), "bacd")
        s = "dcab"
        pairs = [[0, 3], [1, 2], [0, 2]]
        self.assertEqual(self.s.smallestStringWithSwaps(s, pairs), "abcd")
        s = "cba"
        pairs = [[0, 1], [1, 2]]
        self.assertEqual(self.s.smallestStringWithSwaps(s, pairs), "abc")


if __name__ == "__main__":
    main()
