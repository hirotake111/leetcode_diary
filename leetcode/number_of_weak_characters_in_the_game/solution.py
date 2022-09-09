from typing import List, Tuple
from unittest import TestCase, main


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        tmp_max_defense, cur_max_defense = 0, 0
        answer = 0
        properties.sort(reverse=True)
        prev_attack = properties[0][0]

        for attack, defense in properties:
            if attack < prev_attack:
                cur_max_defense = max(cur_max_defense, tmp_max_defense)
            if defense < cur_max_defense:
                answer += 1
            tmp_max_defense = max(defense, tmp_max_defense)
            prev_attack = attack

        return answer


class Test(TestCase):
    data: List[Tuple[List[List[int]], int]] = [
        ([[2, 2], [3, 3]], 1),
        ([[1, 1], [2, 1], [2, 2], [1, 2]], 1),
    ]

    def test_solution(self):
        s = Solution()
        for input, expected in self.data:
            self.assertEqual(s.numberOfWeakCharacters(input), expected)


if __name__ == "__main__":
    main()
