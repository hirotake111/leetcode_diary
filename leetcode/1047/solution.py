from typing import List


class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack: List[str] = []

        for c in s:
            if stack == []:
                stack.append(c)
            elif stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)

        return "".join(stack)
