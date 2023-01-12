"""
https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
1519. Number of Nodes in the Sub-Tree With the Same Label

You are given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a lower-case character given in the string labels (i.e. The node with the number i has the label labels[i]).

The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the tree.

Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label as node i.

A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        answer = [0] * n

        # Crate a tree
        tree: List[List[int]] = [[] for _ in range(n)]
        for a, b in edges:
            if a not in tree[b]:
                tree[b].append(a)
            if b not in tree[a]:
                tree[a].append(b)

        def dfs(current: int, parent: int) -> List[int]:
            counts = [0] * 26  # a - z
            # dfs the child edges first
            for child in tree[current]:
                if child != parent:
                    result = dfs(child, current)
                    # combine returned result and counts
                    counts = [a + b for a, b in zip(counts, result)]

            # Identify index of counts
            idx = ord(labels[current]) - 97
            # increment counts array
            counts[idx] += 1
            # update answer
            answer[current] = counts[idx]
            return counts

        dfs(0, -1)
        return answer


class Test(TestCase):
    data: List[Tuple[int, List[List[int]], str, List[int]]] = [
        (
            7,
            [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
            "abaedcd",
            [2, 1, 1, 1, 1, 1, 1],
        ),
        (4, [[0, 1], [1, 2], [0, 3]], "bbbb", [4, 2, 1, 1]),
    ]

    def test_solution(self):
        s = Solution()
        for n, edges, labels, expected in self.data:
            self.assertEqual(s.countSubTrees(n, edges, labels), expected)


if __name__ == "__main__":
    main()
