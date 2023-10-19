"""
https://leetcode.com/problems/validate-binary-tree-nodes/
1361. Validate Binary Tree Nodes
"""


class UnionFind:
    def __init__(self, n: int):
        self.roots = [i for i in range(n)]

    def find(self, i: int) -> int:
        if self.roots[i] != i:
            self.roots[i] = self.find(self.roots[i])
        return self.roots[i]

    def union(self, p: int, c: int) -> bool:
        rp, rc = self.find(p), self.find(c)
        if c != rc:
            # child node already has a parent node
            return False
        if c == rp:
            # two nodes form bidirectional edge
            return False
        self.roots[rc] = rp
        return True


class Solution:
    def validateBinaryTreeNodes(
        self, n: int, leftChild: List[int], rightChild: List[int]
    ) -> bool:
        uf = UnionFind(n)
        for parent in range(n):
            if leftChild[parent] >= 0:
                if not uf.union(parent, leftChild[parent]):
                    return False
            if rightChild[parent] >= 0:
                if not uf.union(parent, rightChild[parent]):
                    return False

        return len(set(uf.find(i) for i in uf.roots)) == 1
