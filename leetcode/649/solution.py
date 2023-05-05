"""
https://leetcode.com/problems/dota2-senate/description/
649. Dota2 Senate

In the world of Dota2, there are two parties: the Radiant and the Dire.

The Dota2 senate consists of senators coming from two parties. Now the Senate wants to decide on a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

Ban one senator's right: A senator can make another senator lose all his rights in this and all the following rounds.
Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.
Given a string senate representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are n senators, the size of the given string will be n.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for his own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".
"""
from collections import Counter


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        senators = Counter(senate)
        banned = {"R": 0, "D": 0}
        queue = [*senate]

        while senators["R"] > 0 and senators["D"] > 0:
            s = queue.pop(0)
            if banned[s] > 0:
                # s is banned -> decrement senators and banned
                senators[s] -= 1
                banned[s] -= 1
                continue
            # s is not banned -> increment banned[opponent] and push it to the queue again
            o = "R" if s == "D" else "D"
            banned[o] += 1
            queue.append(s)

        return "Radiant" if senators["R"] > 0 else "Dire"
