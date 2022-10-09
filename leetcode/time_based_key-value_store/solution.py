from symbol import return_stmt
from typing import Dict, List, Optional


class TreeNode:
    val: str
    timestamp: int
    left: Optional["TreeNode"]
    right: Optional["TreeNode"]

    def __init__(self, val: str, timestamp: int) -> None:
        self.val = val
        self.timestamp = timestamp
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return (
            f"t: {self.timestamp}, v: {self.val}, left: {self.left} right: {self.right}"
        )


class TimeMap:
    map: Dict[str, List[str]]
    tail: int

    def __init__(self):
        self.values =[ ]
        self.tail = -1

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values.append(value)
        self.tail += 1


    def get(self, key: str, timestamp: int) -> str:
        root = self.map.get(key)
        if root is None:
            return ""
        return self._dfs_get(root, timestamp)

    def _dfs_get(self, node: TreeNode, timestamp: int) -> str:
        

    def _dfs(self, node: TreeNode, root: TreeNode) -> None:
        if root.timestamp <= node.timestamp:
            if root.right is None:  # append node to the right
                root.right = node
            else:  # search for the higher node
                self._dfs(node, root.right)
            return
        # node.val < root.val
        if root.left is None:  # append node to the left
            root.left = node
        else:
            # dig search for lower node
            self._dfs(node, root.left)


if __name__ == "__main__":
    t = TimeMap()
    t.set("a", "foo", 3)
    # t.set("b", "bar", 1)
    t.set("a", "foo", 1)
    print(t.map["a"])


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
