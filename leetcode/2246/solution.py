"""
https://leetcode.com/problems/longest-path-with-different-adjacent-characters/
2246. Longest Path With Different Adjacent Characters
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        answer = [0]

        # Create a tree out of parent array
        tree: List[List[int]] = [[] for _ in range(len(s))]
        for cld, prt in enumerate(parent):
            if prt != -1:
                tree[prt].append(cld)

        def dfs(idx: int) -> int:
            """returns the longest path length"""
            longest_1, longest_2 = 0, 0

            if len(tree[idx]) == 0:
                # No child nodes -> return 1 (itself)
                return 1

            # Iterate over child nodes and update 1st and 2nd logest paths
            for child in tree[idx]:
                result = dfs(child)

                if s[idx] == s[child]:
                    # Just update answer and then go to next
                    answer[0] = max(answer[0], result)
                    continue

                # Update longest paths
                longest_1, longest_2 = swap(longest_1, longest_2, result)

            # Update answer (compare current result and child-parent-child)
            answer[0] = max(answer[0], longest_1 + 1 + longest_2)
            return longest_1 + 1  # longest + parent

        # Edge case: only one node
        if len(tree) == 1:
            return 1

        dfs(0)
        return answer[0]


def swap(longest_1: int, longest_2: int, candidate: int) -> Tuple[int, int]:
    if candidate < longest_2:
        return longest_1, longest_2
    if longest_1 < candidate:
        return candidate, longest_1
    return longest_1, candidate


class Test(TestCase):
    data: List[Tuple[List[int], str, int]] = [
        ([-1, 0, 0, 1, 1, 2], "abacbe", 3),
        ([-1, 0, 1], "aab", 2),
    ]

    def test_solution(self):
        s = Solution()
        for a, b, c in self.data:
            self.assertEqual(s.longestPath(a, b), c)


if __name__ == "__main__":
    main()
