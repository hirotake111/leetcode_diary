"""
https://leetcode.com/problems/clone-graph/
133. Clone Graph

Given a reference of a node in a connected undirected graph.
Return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
"""


# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: "Node") -> "Node":
        seen = {}

        # Edge case
        if node is None:
            return None

        def dfs(original: Node, cloned: Node):
            for neighbor in original.neighbors:
                if neighbor.val not in seen:
                    cloned_neighbor = Node(neighbor.val, [])
                    cloned_neighbor.neighbors.append(cloned)
                    cloned.neighbors.append(cloned_neighbor)
                    seen[neighbor.val] = cloned_neighbor
                    dfs(neighbor, cloned_neighbor)

                cloned_neighbor = seen[neighbor.val]
                # In case the graph forms a circle,
                # we need to check if the cloned neighbor is connected to cloned node
                if cloned_neighbor not in cloned.neighbors:
                    cloned.neighbors.append(cloned_neighbor)

        head = Node(node.val, [])
        seen[node.val] = head
        dfs(node, head)
        return head
