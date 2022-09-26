from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        """union find approach"""

        def rank(ch: str) -> int:
            """takes character and returns corresponding integer"""
            return ord(ch) - 97  # ord("a")

        def find(n: int) -> int:
            """returns value of (current) root element"""
            if parent[n] == n:
                return n
            parent[n] = find(parent[n])
            return parent[n]

        # each element in this list stores parent element so we can track the root element
        # if it's a root, then it should be parent[i] = i, therefore initially all elements are parent[i] = i
        parent = [i for i in range(26)]

        # union phase (handle == caases)
        for e in equations:
            if e[1] == "=":
                # group a and b together
                parent[find(rank(e[0]))] = find(rank(e[3]))

        # handle != cases
        for e in equations:
            if e[1] == "!" and find(rank(e[0])) == find(rank(e[3])):
                return False

        return True


class Test(TestCase):
    data: List[Tuple[List[str], bool]] = [
        (["a==b", "b!=a"], False),
        (["b==a", "a==b"], True),
        (
            [
                "a==b",
                "d==a",
                "b==c",
                "c==d",
            ],
            True,
        ),
    ]

    def test_solution(self):
        s = Solution()
        for equations, expected in self.data:
            self.assertEqual(s.equationsPossible(equations), expected)


if __name__ == "__main__":
    main()
