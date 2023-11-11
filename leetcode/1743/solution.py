"""
https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/
1743. Restore the Array From Adjacent Pairs
"""
from typing import List
from collections import defaultdict


class Solution:
    def restoreArray(self, pairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        # seen will be used to:
        # 1. identify two elements that only have one neighbor (the beginning and the end of the array)
        # 2. prevent loop in the last while loop
        seen = set()

        for i, j in pairs:
            graph[i].append(j)
            graph[j].append(i)
            if i in seen:
                seen.remove(i)
            else:
                seen.add(i)
            if j in seen:
                seen.remove(j)
            else:
                seen.add(j)

        current = seen.pop()
        arr = [current]
        end = seen.pop()

        while current != end:
            seen.add(current)
            pair = graph[current]
            current = pair[1] if len(pair) == 2 and pair[1] not in seen else pair[0]
            arr.append(current)

        return arr
