"""
https://leetcode.com/problems/design-hashmap/
706. Design HashMap
"""
HASH = 1000
class MyHashMap:

    def __init__(self):
        self.arr = [None] * HASH 

    def put(self, key: int, value: int) -> None:
        hashed = key % HASH 
        node = self.arr[hashed]
        if node is None:
            self.arr[hashed] = LinkedList(key, value)
            return
        if node.key == key:
            node.value = value
            return
        while node.next:
            node = node.next
            if node.key == key:
                node.value = value
                return
        node.next = LinkedList(key, value)
        

    def get(self, key: int) -> int:
        hashed = key % HASH
        node = self.arr[hashed]
        while node:
            if node.key == key:
                return node.value
            node = node.next 
        return -1
        

    def remove(self, key: int) -> None:
        hashed = key % HASH
        head = self.arr[hashed]
        if head is None or head is None:
            return
        if head.key == key:
            self.arr[hashed] = head.next
            return
        prev, node = head, head.next
        while node:
            if node.key == key:
                prev.next = node.next
                return
            prev = node
            node = node.next


        
class LinkedList:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
    
    def __repr__(self):
        return f"<{self.value}, {self.next}>"


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)