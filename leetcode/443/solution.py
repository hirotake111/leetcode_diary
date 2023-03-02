"""
https://leetcode.com/problems/string-compression/
443. String Compression
Given an array of characters chars, compress it using the following algorithm:

Begin with an empty string s. For each group of consecutive repeating characters in chars:

If the group's length is 1, append the character to s.
Otherwise, append the character followed by the group's length.
The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.

After you are done modifying the input array, return the new length of the array.

You must write an algorithm that uses only constant extra space.
"""
from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        i, j = 0, 0

        while j < len(chars):
            # Set the first character to i
            chars[i], k = chars[j], j
            count, i, j = 1, i + 1, j + 1

            # Count the number of consecutive repeating characters
            while j < len(chars) and chars[j] == chars[k]:
                count, j = count + 1, j + 1

            if 1 < count:
                # set count to chars[i] (consider count's)
                for c in str(count):
                    chars[i], i = c, i + 1

        return i
