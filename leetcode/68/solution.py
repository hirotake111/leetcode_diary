"""
https://leetcode.com/problems/text-justification/
68. Text Justification
"""
from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        # Group words
        lines = []
        line = []
        current_width = 0
        i = 0
        for word in words:
            if current_width == 0:
                line.append(word)
                current_width += len(word)
            elif current_width + len(word) + 1 <= maxWidth:
                # Append the word to the current group
                line.append(word)
                current_width += len(word) + 1
            else:
                # Append the word to a new group
                lines.append(line)
                line = [word]
                current_width = len(word)
        lines.append(line)

        # Pad spaces
        justified = []
        for i in range(len(lines)):
            if i == len(lines) - 1 or len(lines[i]) == 1:
                # The last line or only one word in the line
                text = " ".join(lines[i])
                justified.append(text + " " * (maxWidth - len(text)))
            else:
                line = lines[i]
                num_of_sp = maxWidth - sum([len(c) for c in line])
                between_words = len(line) - 1
                base, extra = divmod(num_of_sp, between_words)
                spaces = [" " * base for _ in range(between_words)]
                for j in range(extra):
                    spaces[j] += " "
                spaces.append("")
                text = "".join([line[k] + spaces[k] for k in range(len(line))])
                justified.append(text)

        return justified
