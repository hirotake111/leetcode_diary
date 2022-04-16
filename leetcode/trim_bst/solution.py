from typing import List, Optional, cast
from unittest import main, TestCase
from queue import Queue

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"<{self.val}, {self.left}, {self.right}>"


def createBST(arr: List[Optional[int]]) -> Optional[TreeNode]:
    queue: Queue[TreeNode] = Queue(0)
    if len(arr) == 0:
        return None
    node = TreeNode(val=arr[0])
    root = node
    queue.put(node)
    i = 1
    l = len(arr)
    while i < l:
        parent = queue.get()
        node = TreeNode(val=arr[i]) if i is not None else None
        parent.left = node
        queue.put(node)
        i += 1
        if i >= l:
            break
        node = TreeNode(val=arr[i]) if i is not None else None
        parent.right = node
        queue.put(node)
        i += 1

    return root

    # root = None
    # prev = None
    # for i in arr:
    #     node = TreeNode(val=i)
    #     if root is None:
    #         root = node
    #         prev = node
    #         continue
    #     while True:
    #         if prev.val > node.val:
    #             if prev.left is None:
    #                 prev.left = node
    #                 break
    #             # prev.left exists
    #             prev = prev.left
    #             continue
    #         # prev.val < node.val
    #         if prev.right is None:
    #             prev.right = node
    #             break
    #         # prev.right exits
    #         prev = prev.right

    #     prev = node
    # return cast(TreeNode, root)

    # if len(arr) == 0:
    #     # no item left -> return root
    #     return TreeNode() if root is None else root

    # # item left -> create a new treeNode
    # node = TreeNode(val=arr[0])
    # if root is None:
    #     # new node will be root
    #     return createBST(arr[1:], node)
    # # root is there, and we have a new node now
    # current = root
    # while True:
    #     if current.val > node.val:
    #         current


class Solution:
    def trimBST(
        self, root: Optional[TreeNode], low: int, high: int
    ) -> Optional[TreeNode]:
        def get_highest_node(node: Optional[TreeNode], high: int):
            root = node
            while True:
                if node is None:
                    return

        if root is None:
            return None
        node = root
        prev = None
        while True:
            if node.val < low:
                # node should be removed
                # if node has right child, find a node with
                # highest number less than high
                if prev:
                    prev.left = get_highest_node(node, low)
                    break
                # prev is None -> this is root node
                return None
                if node.right:
                    pass

        return root


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        root = [1, 0, 2]
        expected = createBST([1, None, 2])
        self.assertEqual(self.s.trimBST(root, low=1, high=2))
        pass


if __name__ == "__main__":
    # main()
    print(createBST([3, 0, 4, None, 2, None, None, 1]))
