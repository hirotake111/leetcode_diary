from collections import defaultdict
import re
from typing import DefaultDict, List, Tuple
from unittest import TestCase, main


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d: DefaultDict[str, List[str]] = defaultdict(list)

        def has_duplicates(arr: List[str]) -> bool:
            return 1 < len(arr)

        for _path in paths:
            path = _path.split(" ")
            directory = path[0]
            files = path[1:]
            for file in files:
                filename, content = file.split("(")
                content = content[:-1]
                d[content].append(f"{directory}/{filename}")

        return list(filter(has_duplicates, [v for v in d.values()]))


class Test(TestCase):
    data: List[Tuple[List[str], List[List[str]]]] = [
        (
            [
                "root/a 1.txt(abcd) 2.txt(efgh)",
                "root/c 3.txt(abcd)",
                "root/c/d 4.txt(efgh)",
                "root 4.txt(efgh)",
            ],
            [
                ["root/a/2.txt", "root/c/d/4.txt", "root/4.txt"],
                ["root/a/1.txt", "root/c/3.txt"],
            ],
        ),
        (
            [
                "root/a 1.txt(abcd) 2.txt(efgh)",
                "root/c 3.txt(abcd)",
                "root/c/d 4.txt(efgh)",
            ],
            [["root/a/2.txt", "root/c/d/4.txt"], ["root/a/1.txt", "root/c/3.txt"]],
        ),
    ]

    def test_solution(self):
        s = Solution()
        for input, expected in self.data:
            self.assertEqual(s.findDuplicate(input), expected)


if __name__ == "__main__":
    main()
