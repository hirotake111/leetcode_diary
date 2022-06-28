from collections import Counter
from heapq import heapify, heappop
from typing import List, Set, Tuple
from unittest import TestCase, main


class Solution:
    def minDeletions(self, s: str) -> int:
        delete_count = 0
        seen: Set[int] = set()

        for n in [v for v in Counter(s).values()]:
            while n in seen:
                n -= 1
                delete_count += 1
                if n == 0:
                    break
            seen.add(n)

        return delete_count

        # ans, current = 0, 100001
        # counter = Counter(s)
        # heap = [-v for v in counter.values()]
        # heapify(heap)
        # length = len(heap)

        # while length > 0:
        # n = -heappop(heap)
        # if current > n:
        # current = n
        # elif current > 0:
        # current -= 1
        # diff = n - current
        # ans += diff
        # else:
        # ans += n
        # length -= 1

        # return ans

        # first approach
        # ans, current = 0, 100001
        # counter = Counter(s)
        # frequency_arr = sorted([v for v in counter.values()], reverse=True)

        # for n in frequency_arr:
        # if current > n:
        # current = n
        # continue

        # if current > 0:
        # current -= 1
        # diff = n - current
        # ans += diff
        # continue

        # ans += n

        # return ans


class Test(TestCase):
    s = Solution()
    data: List[Tuple[str, int]] = [
        ("abcd", 3),
        ("aaabbbcccddd", 6),
        ("aab", 0),
        ("aaabbbcc", 2),
        ("ceabaacb", 2),
    ]

    def test_solution(self):
        for input, expected in self.data:
            self.assertEqual(self.s.minDeletions(input), expected)


if __name__ == "__main__":
    main()
