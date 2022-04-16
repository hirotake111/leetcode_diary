from typing import List, Optional
from unittest import main, TestCase
from queue import Queue


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue: List[TreeNode] = []
        n = 0

        if root is None:
            return None

        def dfs(root: TreeNode):
            if root.left:
                dfs(root.left)
            queue.insert(0, root)
            if root.right:
                dfs(root.right)

        dfs(root)

        for node in queue:
            n += node.val
            node.val = n
        return root

        """
        initial version
        """
        # stack: List[TreeNode] = [cast(TreeNode, root)]
        # queue: List[TreeNode] = []
        # visited: List[TreeNode] = []
        # n = 0

        # if root is None:
        #     return root

        # # put all value to queue
        # while len(stack) != 0:
        #     node = stack.pop()
        #     if not node in visited and node.left:
        #         visited.append(node)
        #         stack.append(node)
        #         stack.append(node.left)
        #         continue
        #     # node doesn't have left node
        #     queue = [node] + queue

        #     if node.right:
        #         stack.append(node.right)

        # # iterate queue in reverse order
        # for node in queue:
        #     n += node.val
        #     node.val = n

        # return root


class TestSolution(TestCase):
    s = Solution()

    def test_solution(self):
        # arr = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
        # bst = list_to_bst(arr)
        # l = bst_to_list(bst)
        arr = [4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8]
        expected = [
            30,
            36,
            21,
            36,
            35,
            26,
            15,
            None,
            None,
            None,
            33,
            None,
            None,
            None,
            8,
        ]
        root = list_to_bst(arr)
        self.assertEqual(bst_to_list(self.s.convertBST(root)), expected)


def list_to_bst(arr: List[int]) -> TreeNode:
    queue: Queue[TreeNode] = Queue()
    root = TreeNode(val=arr[0])
    queue.put(root)
    i, l = 0, len(arr)
    while i < l:
        i += 1
        if i >= l:
            break
        node = queue.get()
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
    queue: Queue[TreeNode] = Queue()
    queue.put(root)
    while not queue.empty():
        node = queue.get()
        if node is not None:
            arr.append(node.val)
            queue.put(node.left)
            queue.put(node.right)
        else:
            arr.append(None)
    i = len(arr) - 1  # last index of arr

    while True:
        if arr[i] is not None:
            # this is the index we are looking for
            break
        i -= 1

    return arr[: i + 1]


if __name__ == "__main__":
    main()
