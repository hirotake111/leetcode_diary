"""
https://leetcode.com/problems/validate-stack-sequences/
946. Validate Stack Sequences

Given two integer arrays pushed and popped each with distinct values, 
return true if this could have been the result of a sequence of push and pop operations on an initially empty stack, or false otherwise.
"""
from typing import List


class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack: List[int] = []
        i = j = 0

        # Perform all the push operations to the stack
        while i < len(pushed):
            # Check to see if we could do a pop operation
            if len(stack) and stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                # We do a push operation
                stack.append(pushed[i])
                i += 1

        # There might be some pop operations left
        while j < len(popped):
            # If the top of the stack is not same as pop[j],
            # then we cannot proceed further operations anymore -> return False
            if stack[-1] != popped[j]:
                return False
            stack.pop()
            j += 1

        # All push and pop operations are done!
        return True
