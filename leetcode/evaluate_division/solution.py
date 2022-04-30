from typing import Dict, List, Set, Tuple
from unittest import main, TestCase


class Solution:
    def calcEquation(
        self, equations: List[List[str]], values: List[float], queries: List[List[str]]
    ) -> List[float]:
        graph: Dict[str, List[Tuple[str, float]]] = {}
        ans: List[float] = [-1.0] * len(queries)
        all_vars: Set[str] = set()

        # create graph
        for i, (x, y) in enumerate(equations):
            all_vars.add(x)
            all_vars.add(y)
            if graph.get(x):
                graph[x].append((y, values[i]))
            else:
                graph[x] = [(y, values[i])]

            if graph.get(y):
                graph[y].append((x, 1 / values[i]))
            else:
                graph[y] = [(x, 1 / values[i])]
            # if len(x) > 1:

        for i, (x, y) in enumerate(queries):
            if x not in all_vars or y not in all_vars:
                continue

            if [x, y] in equations:
                idx = equations.index([x, y])
                ans[i] = values[idx]
                continue

            if [y, x] in equations:
                idx = equations.index([y, x])
                ans[i] = 1 / values[idx]
                continue

            if x == y:
                ans[i] = 1.0
                continue

            visited: List[str] = []

            def dfs(node: str, current: float):
                if node == y:
                    return current
                if node in visited or graph.get(node) is None:
                    return -1.0

                # x is still not visited, and in graph
                for next, val in graph[node]:
                    visited.append(node)
                    result = dfs(next, current * val)
                    if result != -1.0:
                        return result
                return -1.0

            ans[i] = dfs(x, 1.0)

        return ans


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        # equations = [["a", "b"], ["b", "c"]]
        # values = [2.0, 3.0]
        # queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
        # expected = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
        # self.assertEqual(self.s.calcEquation(equations, values, queries), expected)

        # equations = [["a", "b"], ["b", "c"], ["bc", "cd"]]
        # values = [1.5, 2.5, 5.0]
        # queries = [["a", "c"], ["c", "b"], ["bc", "cd"], ["cd", "bc"]]
        # expected = [3.75000, 0.40000, 5.00000, 0.20000]
        # self.assertEqual(self.s.calcEquation(equations, values, queries), expected)

        # equations = [["a", "b"]]
        # values = [0.5]
        # queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
        # expected = [0.50000, 2.00000, -1.00000, -1.00000]
        # self.assertEqual(self.s.calcEquation(equations, values, queries), expected)

        # equations = [["a", "e"], ["b", "e"]]
        # values = [4.0, 3.0]
        # queries = [["a", "b"], ["e", "e"], ["x", "x"]]
        # expected = [6.00000, 0.50000, -1.00000, 1.00000, -1.00000]
        # self.assertEqual(self.s.calcEquation(equations, values, queries), expected)

        equations = [["x1", "x2"], ["x2", "x3"], ["x3", "x4"], ["x4", "x5"]]
        values = [3.0, 4.0, 5.0, 6.0]
        queries = [
            ["x1", "x5"],
            ["x5", "x2"],
            ["x2", "x4"],
            ["x2", "x2"],
            ["x2", "x9"],
            ["x9", "x9"],
        ]
        expected = [360.00000, 0.00833, 20.00000, 1.00000, -1.00000, -1.00000]
        self.assertEqual(self.s.calcEquation(equations, values, queries), expected)


if __name__ == "__main__":
    main()
