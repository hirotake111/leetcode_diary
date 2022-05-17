# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(
        self, original: TreeNode, cloned: TreeNode, target: TreeNode
    ) -> TreeNode:
        """dfs approach #2"""
        so: List[TreeNode] = [original]
        sc: List[TreeNode] = [cloned]

        while so:
            no = so.pop()
            nc = sc.pop()

            if no == target:
                return nc

            if no.right:
                so.append(no.right)
                sc.append(nc.right)
            if no.left:
                so.append(no.left)
                sc.append(nc.left)

        raise Exception("error")

        # """dfs approach #1"""
        # def dfs(o: TreeNode, c: TreeNode):
        #     if o == target:
        #         return c

        #     if o.left:
        #         res = dfs(o.left, c.left)
        #         if res:
        #             return res

        #     if o.right:
        #         return dfs(o.right, c.right)

        # return dfs(original, cloned)

        # """bfs approach"""
        # qo: List[TreeNode] = [original]
        # qc: List[TreeNode] = [cloned]

        # while True:
        #     no = qo.pop(0)
        #     nc = qc.pop(0)

        #     if no == target:
        #         return nc

        #     if no.left is not None:
        #         qo.append(no.left)
        #         qc.append(nc.left)

        #     if no.right is not None:
        #         qo.append(no.right)
        #         qc.append(nc.right)
