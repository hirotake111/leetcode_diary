from typing import List, Tuple, Set
from unittest import TestCase, main


class Solution:
    def numSquares(self, n: int) -> int:
        i, count = 1, 0
        candidates: List[int] = []
        visited: Set[int] = set()  # just to avoid calculating the same value

        # create a candidate list beforehand
        while i * i <= n:
            candidates.append(i * i)
            i += 1

        queue = [n]
        while queue != []:
            count += 1

            # iterate just len(queue) times
            for _ in range(len(queue)):
                queue_value = queue.pop(0)  # previouly, it was rest
                # pick up one from candidate list
                for candidate in candidates:
                    rest = queue_value - candidate
                    # if already visited, go to the next value
                    if rest in visited:
                        continue
                    # if the rest equals 0, then we find the answer -> return count
                    if rest == 0:
                        return count
                    # if rest is less than 0, we no longer need to iterate over candidate list -> move to the next queue_value
                    if rest < 0:
                        break
                    # we can still subtract it with one of candidates -> add it to the queue
                    visited.add(rest)
                    queue.append(rest)

        # this should not be possible to reach this line
        raise Exception


class Test(TestCase):
    data_set: List[Tuple[int, int]] = [
        (7168, 4),
        (12, 3),
    ]

    def test_solution(self):
        s = Solution()
        for given, expected in self.data_set:
            self.assertEqual(s.numSquares(given), expected)


if __name__ == "__main__":
    main()
