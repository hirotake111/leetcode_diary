from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def dfs(i: int, j: int, k: int):
            directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
            if k == len(word):  # we found the word!
                return True
            if i < 0 or m <= i or j < 0 or n <= j:  # out of board
                return False
            if board[i][j] != word[k]:  # the word doesnt match
                return False

            # now we want to mark the current character (position) as visited
            # (in order to prevent a circular search)
            # but it could be used for other search
            # store it temporarily and restore it at the end of the func.
            tmp = board[i][j]
            board[i][j] = "."

            for x, y in directions:
                if dfs(i + x, j + y, k + 1):
                    return True
            # restore the character for future use
            board[i][j] = tmp

        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False
