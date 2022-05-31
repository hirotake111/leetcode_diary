from typing import List, Set, Tuple, Dict
from unittest import TestCase, main


class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        l = len(s)
        st: Set[str] = set()
        for i in range(l - k + 1):
            st.add(s[i : i + k])

        return len(st) == 2**k


#        d: Dict[str, bool] = {}

# def func(st: str, n: int):
# if n == 0:
## add key to the dict
# d[st] = False
# return
# func(f"{st}0", n - 1)
# func(f"{st}1", n - 1)

## generate and add possible keys to dict
# func("", k)
## iterate over s
# for i in range(0, len(s) - k + 1):
# d[s[i : i + k]] = True
## check if d has any key containing 0
# for k, v in d.items():
# if not v:
# return False
# return True


class Test(TestCase):
    s = Solution()
    data: List[Tuple[str, int, bool]] = [
        ("00110", 2, True),
        ("00110110", 2, True),
        ("0110", 1, True),
        ("0110", 2, False),
    ]

    def test_solution(self):
        for s, k, expected in self.data:
            self.assertEqual(self.s.hasAllCodes(s, k), expected)


if __name__ == "__main__":
    main()
