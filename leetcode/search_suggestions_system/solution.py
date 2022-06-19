from collections import defaultdict
from typing import Dict, List, Tuple
from unittest import TestCase, main


class Solution:
    def suggestedProducts(
        self, products: List[str], searchWord: str
    ) -> List[List[str]]:
        d: Dict[str, List[str]] = defaultdict(list)
        ans: List[List[str]] = [[]] * len(searchWord)

        for product in products:
            for i in range(len(product)):
                substring = product[: i + 1]
                d[substring].append(product)

        for key in d.keys():
            d[key].sort()

        for j in range(len(searchWord)):
            typed = searchWord[: j + 1]
            suggestions = d.get(typed)
            if suggestions:
                ans[j] = suggestions[:3]

        return ans
        # # faster version
        # return [
        #     d[searchWord[: j + 1]][:3] if d.get(searchWord[: j + 1]) else []
        #     for j in range(len(searchWord))
        # ]


class Test(TestCase):
    s = Solution()
    data: List[Tuple[List[str], str, List[List[str]]]] = [
        (
            ["mobile", "mouse", "moneypot", "monitor", "mousepad"],
            "mouse",
            [
                ["mobile", "moneypot", "monitor"],
                ["mobile", "moneypot", "monitor"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
                ["mouse", "mousepad"],
            ],
        ),
        (
            ["havana"],
            "havana",
            [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]],
        ),
        (
            ["bags", "baggage", "banner", "box", "cloths"],
            "bags",
            [
                ["baggage", "bags", "banner"],
                ["baggage", "bags", "banner"],
                ["baggage", "bags"],
                ["bags"],
            ],
        ),
        (["havana"], "tatiana", [[], [], [], [], [], [], []]),
    ]

    def test_solution(self):
        for products, search_word, expected in self.data:
            self.assertEqual(self.s.suggestedProducts(products, search_word), expected)


if __name__ == "__main__":
    main()
