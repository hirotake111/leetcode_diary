"""
https://leetcode.com/problems/count-vowels-permutation/
1220. Count Vowels Permutation
"""


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """Initial solution"""
        MOD = 10**9 + 7
        arr = [1] * 5  # [a,e,i,o,u]
        a, e, i, o, u = 0, 1, 2, 3, 4

        for _ in range(n - 1):
            tmp = [0] * 5
            for idx, n in enumerate(arr):
                if idx == a:
                    tmp[e] += n % MOD  # a -> e
                elif idx == e:
                    tmp[a] += n % MOD  # e -> a
                    tmp[i] += n % MOD  # e -> i
                elif idx == i:
                    tmp[a] += n % MOD  # i -> a
                    tmp[e] += n % MOD  # i -> e
                    tmp[o] += n % MOD  # i -> o
                    tmp[u] += n % MOD  # i -> u
                elif idx == o:
                    tmp[i] += n % MOD  # o -> i
                    tmp[u] += n % MOD  # o -> u
                else:  # idx == u(4)
                    tmp[a] += n % MOD  # u -> a
                arr = tmp

        return sum(arr) % MOD


class Solution:
    def countVowelPermutation(self, n: int) -> int:
        """Optimized solution"""
        MOD = 10**9 + 7
        a = e = i = o = u = 1

        for _ in range(n - 1):
            a, e, i, o, u = (
                (e + i + u) % MOD,
                (a + i) % MOD,
                (e + o) % MOD,
                i,
                (i + o) % MOD,
            )

        return (a + e + i + o + u) % MOD
