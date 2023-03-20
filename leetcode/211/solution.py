"""
https://leetcode.com/problems/design-add-and-search-words-data-structure/
211. Design Add and Search Words Data Structure
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
"""
from collections import defaultdict


class Node:
    def __init__(self):
        self.next = [None] * 26
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = Node()

    def addWord(self, word: str) -> None:
        node = self.root
        for c in word:
            i = ord(c) - 97
            if node.next[i] is None:
                node.next[i] = Node()
            node = node.next[i]
        node.end = True

    def search(self, word: str) -> bool:
        def _search(i: int, node: Node) -> bool:
            if i == len(word):
                return node.end
            if word[i] == ".":
                # wild card
                for n in filter(lambda x: x, node.next):
                    if _search(i + 1, n):
                        return True
                return False
            # a-z
            j = ord(word[i]) - 97
            if node.next[j] is None:
                # Not found
                return False
            return _search(i + 1, node.next[j])

        return _search(0, self.root)


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
