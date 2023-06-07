class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0
        while a + b + c:
            if c & 1:
                # Either a or b must be 1
                # -> add 1 if both a and b are 0
                flips += not ((a & 1) | (b & 1))
            else:
                # both a and b must be 0
                # -> add 1 if each of a and b is 0, respectively
                flips += (a & 1) + (b & 1)
            a, b, c = a >> 1, b >> 1, c >> 1
        return flips
