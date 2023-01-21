"""
https://leetcode.com/problems/restore-ip-addresses/
93. Restore IP Addresses
A valid IP address consists of exactly four integers separated by single dots. Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.

For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245", "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
Given a string s containing only digits, return all possible valid IP addresses that can be formed by inserting dots into s. You are not allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        answer: List[str] = []

        # Edge cases
        if len(s) < 4:
            return []
        if 12 < len(s):
            return []

        def is_valid(address: str) -> bool:
            if len(address) == 1:
                return True
            if address[0] == "0":
                # 0x or 0xx -> invalid
                return False
            if len(address) == 2 and address[0] in "123456789":
                return True
            if int(address) <= 255:
                return True
            return False

        def restore(idx: int, octet: int, current: str):
            if len(s) <= idx:
                # Out of index
                return

            if octet == 4:
                # Last octet
                if is_valid(s[idx:]):
                    answer.append(f"{current}{s[idx:]}")
                return

            # 1st, 2nd, or 3rd octet
            restore(idx + 1, octet + 1, f"{current}{s[idx]}.")
            if is_valid(s[idx : idx + 2]):
                restore(idx + 2, octet + 1, f"{current}{s[idx:idx + 2]}.")
            if is_valid(s[idx : idx + 3]):
                restore(idx + 3, octet + 1, f"{current}{s[idx:idx + 3]}.")

        restore(0, 1, "")
        return answer


class Test(TestCase):
    data: List[Tuple[str, List[str]]] = [
        ("25525511135", ["255.255.11.135", "255.255.111.35"]),
        (
            "0000",
            ["0.0.0.0"],
        ),
        ("101023", ["1.0.10.23", "1.0.102.3", "10.1.0.23", "10.10.2.3", "101.0.2.3"]),
    ]

    def test_solution(self):
        solution = Solution()
        for s, expected in self.data:
            self.assertEqual(solution.restoreIpAddresses(s), expected)


if __name__ == "__main__":
    main()
