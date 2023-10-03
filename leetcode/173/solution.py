"""
https://leetcode.com/problems/binary-search-tree-iterator/
173. Binary Search Tree Iterator
"""
from typing import List, Optional 
from unittest import main, TestCase
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return f"<{self.val}>"


class BSTIterator:
    stack: List[TreeNode]
    root: Optional[TreeNode]
    smallest: TreeNode

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self._dfs(root)

    def _dfs(self, node: Optional[TreeNode]):
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        node = self.stack.pop()
        # if smallest has right node, add them to stack
        self._dfs(node.right)

        return node.val

    def hasNext(self) -> bool:
        return len(self.stack) != 0


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

"""Input
["BSTIterator", "next", "next", "hasNext", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
[[[7, 3, 15, None, None, 9, 20]], [], [], [], [], [], [], [], [], []]
Output
[None, 3, 7, true, 9, true, 15, true, 20, false]

Explanation
BSTIterator bSTIterator = new BSTIterator([7, 3, 15, None, None, 9, 20]);
bSTIterator.next();    // return 3
bSTIterator.next();    // return 7
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 9
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 15
bSTIterator.hasNext(); // return True
bSTIterator.next();    // return 20
bSTIterator.hasNext(); // return False
"""


class TestSolution(TestCase):
    def test_solution(self):
        input = [7, 3, 15, None, None, 9, 20]
        root = list_to_bst(input)
        bSTIterator = BSTIterator(root=root)
        self.assertEqual(bSTIterator.next(), 3)
        self.assertEqual(bSTIterator.next(), 7)
        self.assertEqual(bSTIterator.hasNext(), True)
        self.assertEqual(bSTIterator.next(), 9)
        self.assertEqual(bSTIterator.hasNext(), True)
        self.assertEqual(bSTIterator.next(), 15)
        self.assertEqual(bSTIterator.hasNext(), True)
        self.assertEqual(bSTIterator.next(), 20)
        self.assertEqual(bSTIterator.hasNext(), False)


def list_to_bst(arr: List[Optional[int]]) -> TreeNode:
    root = TreeNode(val=arr[0])
    queue: Queue[Optional[TreeNode]] = Queue()
    queue.put(root)
    i, l = 0, len(arr)
    while not queue.empty():
        node = queue.get()
        if node is None:
            i += 2
            continue
        i += 1
        if i >= l:
            break
        node.left = TreeNode(val=arr[i]) if arr[i] else None
        queue.put(node.left)

        i += 1
        if i >= l:
            break
        node.right = TreeNode(val=arr[i]) if arr[i] else None
        queue.put(node.right)

    return root


if __name__ == "__main__":
    main()
