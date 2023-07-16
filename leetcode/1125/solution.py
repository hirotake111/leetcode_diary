"""
https://leetcode.com/problems/smallest-sufficient-team/description/
1125. Smallest Sufficient Team

In a project, you have a list of required skills req_skills, and a list of people. The ith person people[i] contains a list of skills that the person has.

Consider a sufficient team: a set of people such that for every required skill in req_skills, there is at least one person in the team who has that skill. We can represent these teams by the index of each person.

For example, team = [0, 1, 3] represents the people with skills people[0], people[1], and people[3].
Return any sufficient team of the smallest possible size, represented by the index of each person. You may return the answer in any order.

It is guaranteed an answer exists.
"""
from typing import List, Set, Dict


class Solution:
    def smallestSufficientTeam(
        self, req_skills: List[str], people: List[List[str]]
    ) -> List[int]:
        all_skills: Set[int] = set()
        for p in people:
            all_skills = all_skills.union(p)

        skill_dict = {skill: i for i, skill in enumerate(all_skills)}

        def to_bits(skills: List[str]) -> int:
            return sum([1 << skill_dict[skill] for skill in skills])

        required = to_bits(req_skills)
        answer = ["x"] * 17
        dp: Dict[int, List[int]] = {}  # {bits: list of people indexes}
        for i, skills in enumerate(people):
            bits = to_bits(skills)
            if bits == required:
                return [i]
            # Pick up mask and people from dp
            # then create and store new combinations to tmp.
            # If target is found, then update answer
            tmp: Dict[int, List[int]] = {}
            for mask, p in dp.items():
                mask = mask | bits
                if mask == required:
                    # Found it
                    if len(p) + 1 < len(answer):
                        answer = p + [i]
                # Not found -> add the combination to dp
                elif mask not in tmp or len(p) + 1 < len(tmp[mask]):
                    tmp[mask] = p + [i]

            # Concatenate dp and tmp
            for mask, p in tmp.items():
                if mask not in dp or len(p) < len(dp[mask]):
                    dp[mask] = p
            # Add itself to dp
            if bits:
                dp[bits] = [i]

        return answer
