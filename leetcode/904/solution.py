"""
https://leetcode.com/problems/fruit-into-baskets/
904. Fruit Into Baskets
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
Given the integer array fruits, return the maximum number of fruits you can pick.
"""
from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        """Two pointers approach"""
        # If we have less than or equal to 2 types of fruits,
        # then simply return the length of the fruits
        if len(set(fruits)) <= 2:
            return len(fruits)

        # Now it is obvious we have more than 2 types of fruits.
        # (also, we are sure that we have more than 2 fruits.)
        # Let's assin index 0 and 1 to i and j respectively.
        i, j = 0, 1

        # But at this moment it's possible fruits[i] and fruits[j] are the same fruit.
        # So let's update j so that it contains a different fruit from i
        while fruits[i] == fruits[j]:
            j += 1

        # Now we have indexes i and j each contains different fruits.
        # It should be the current maximum rows of fruits we can pick so far.
        answer = len(fruits[i : j + 1])
        f_a, f_b = fruits[i], fruits[j]

        # Iterater over the rest of frutis.
        for k in range(j + 1, len(fruits)):
            if fruits[k] in (f_a, f_b):
                # Update max rows of fruits
                answer = max(answer, len(fruits[i : k + 1]))
                # Let j be the index pointing the beginning of current type of fruit
                if fruits[j] != fruits[k]:
                    j = k
                continue
            # Different fruits -> update i, j, f_a, and f_b
            i, j = j, k
            f_a, f_b = fruits[i], fruits[j]

        return answer


class Test(TestCase):
    data: List[Tuple[List[int], int]] = [
        ([0, 1, 6, 6, 4, 4, 6], 5),
        ([3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4], 5),
        ([1, 0, 3, 4, 3], 3),
    ]

    def test_solution(self):
        solution = Solution()
        for fruits, expected in self.data:
            self.assertEqual(solution.totalFruit(fruits), expected)


if __name__ == "__main__":
    main()
