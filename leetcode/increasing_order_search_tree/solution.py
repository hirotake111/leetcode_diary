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


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        queue: List[TreeNode] = []

        def dfs(root: Optional[TreeNode]):
            if root is None:
                return
            dfs(root.left)
            queue.append(root)
            dfs(root.right)

        dfs(root)

        root, prev = queue[0], None
        for node in queue:
            node.left = None
            node.right = None
            if prev:
                prev.right = node
            prev = node

        return root


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        arr = [5, 3, 6, 2, 4, None, 8, 1, None, None, None, 7, 9]
        # self.assertEqual(bst_to_list(list_to_bst(arr)), arr)
        root = list_to_bst(arr)
        expected = [
            1,
            None,
            2,
            None,
            3,
            None,
            4,
            None,
            5,
            None,
            6,
            None,
            7,
            None,
            8,
            None,
            9,
        ]
        result = self.s.increasingBST(root)
        self.assertEqual(bst_to_list(result), expected)


def list_to_bst(arr: List[int]) -> TreeNode:
    queue: Queue[TreeNode] = Queue()
    root = TreeNode(val=arr[0])
    queue.put(root)
    i, l = 0, len(arr)
    while not queue.empty():
        node = queue.get()
        i += 1
        if i >= l:
            break
        if arr[i] is not None:
            node.left = TreeNode(val=arr[i])
            queue.put(node.left)
        i += 1
        if i >= l:
            break
        if arr[i] is not None:
            node.right = TreeNode(val=arr[i])
            queue.put(node.right)
    return root


def bst_to_list(root: TreeNode) -> List[Optional[int]]:
    arr: List[Optional[int]] = []
    queue: List[Optional[TreeNode]] = []
    queue.append(root)
    while len(queue) != 0:
        node = queue.pop()
        if node:
            arr.append(node.val)
        else:
            arr.append(None)
            continue

        queue.insert(0, node.left if node.left else None)
        queue.insert(0, node.right if node.right else None)

    l = len(arr)
    for i in range(l - 1, 0, -1):
        if arr[i] is not None:
            arr = arr[: i + 1]
            break
    return arr


if __name__ == "__main__":
    main()
