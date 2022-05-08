from typing import List, Optional, Union, cast

"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""


class NestedInteger:
    def isInteger(self) -> bool:
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        """
        pass

    def getInteger(self) -> int:
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        """
        pass

    def getList(self) -> List["NestedInteger"]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        """
        pass


class NestedIterator:
    def __init__(self, nestedList: List[NestedInteger]):
        self.nested_list = nestedList
        self.stack: List[NestedInteger] = []

    def next(self) -> int:
        """returns the next integer in the nested list"""
        if self.stack:
            item = self.stack.pop()
            if item.isInteger():
                return item.getInteger()
            else:
                # value is an another nested list
                for child_item in item.getList()[::-1]:
                    self.stack.append(child_item)
                return self.next()

        # stack is empty
        item = self.nested_list.pop(0)
        if item.isInteger():
            return item.getInteger()
        for child_item in item.getList()[::-1]:
            self.stack.append(child_item)
        return self.next()

    def hasNext(self) -> bool:
        def func(a: NestedInteger):
            if a.isInteger():
                return True
            for item in a.getList():
                if func(item):
                    return True
            return False

        for item in self.nested_list:
            if func(item):
                return True
        for item in self.stack:
            if func(item):
                return True
        return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
