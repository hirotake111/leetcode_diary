from typing import Dict, List, Tuple
from unittest import TestCase, main


class WordFilter:
    def __init__(self, words: List[str]):
        self.dict: Dict[Tuple[str, str], int] = {}
        for i, w in enumerate(words):
            l = len(w)
            for j in range(l):
                for k in range(l):
                    key = (w[: j + 1], w[k:])
                    self.dict[key] = i

    def f(self, prefix: str, suffix: str) -> int:
        idx = self.dict.get((prefix, suffix))
        return idx if idx is not None else -1


class Test(TestCase):
    def test_solution(self):
        wf = WordFilter(["apple"])
        self.assertEqual(wf.f("a", "e"), 0)


if __name__ == "__main__":
    main()
# Your WordFilter object will be instantiated and called as such:
# obj = WordFilter(words)
# param_1 = obj.f(prefix,suffix)
