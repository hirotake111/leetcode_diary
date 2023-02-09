"""
https://leetcode.com/problems/naming-a-company/
2306. Naming a Company
You are given an array of strings ideas that represents a list of names to be used in the process of naming a company. The process of naming a company is as follows:

Choose 2 distinct names from ideas, call them ideaA and ideaB.
Swap the first letters of ideaA and ideaB with each other.
If both of the new names are not found in the original ideas, then the name ideaA ideaB (the concatenation of ideaA and ideaB, separated by a space) is a valid company name.
Otherwise, it is not a valid name.
Return the number of distinct valid names for the company.
"""
from typing import List, Tuple, Set
from unittest import TestCase, main
from collections import defaultdict

# from collections import Set


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        groups: List[Set[str]] = [set() for _ in range(26)]  # a-z
        answer = 0
        # Populate groups list
        for idea in ideas:
            # key: head, value: suffix
            head, suffix = idea[0], idea[1:]
            groups[ord(head) - 97].add(suffix)

        # Iterate over groups
        for i in range(0, 25):
            for j in range(i + 1, 26):
                # Find mutual suffixes
                mutuals = len(groups[i] & groups[j])
                answer += (len(groups[i]) - mutuals) * (len(groups[j]) - mutuals) * 2

        return answer


class Test(TestCase):
    data: List[Tuple[List[str], int]] = [
        (["aaa", "baa", "caa", "bbb", "cbb", "dbb"], 2),
        (["coffee", "donuts", "time", "toffee"], 6),
    ]

    def test_solution(self):
        solution = Solution()
        for ideas, expected in self.data:
            self.assertEqual(solution.distinctNames(ideas), expected)


if __name__ == "__main__":
    main()
