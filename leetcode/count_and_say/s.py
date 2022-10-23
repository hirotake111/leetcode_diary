from unittest import TestCase, main


class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        while n > 1:
            tmp = ""
            current = ""
            count = 0
            for c in ans:
                if current is "":  # set current
                    current = c
                    count += 1
                    continue
                if c == current:  # count up current
                    count += 1
                    continue
                # c is different from current
                # concatenate current and count to answer
                tmp += str(count) + current
                #  go to next character
                current = c
                count = 1
            # coancatenate current and count to answer
            tmp += str(count) + current
            n -= 1
            ans = tmp

        return ans


class TestSolution(TestCase):
    s = Solution()

    def test_s(self):
        self.assertEqual(self.s.countAndSay(1), "1")
        self.assertEqual(self.s.countAndSay(2), "11")
        self.assertEqual(self.s.countAndSay(3), "21")
        self.assertEqual(self.s.countAndSay(4), "1211")
        self.assertEqual(self.s.countAndSay(5), "111221")
        self.assertEqual(self.s.countAndSay(6), "312211")
        self.assertEqual(self.s.countAndSay(7), "13112221")


if __name__ == "__main__":
    main()
