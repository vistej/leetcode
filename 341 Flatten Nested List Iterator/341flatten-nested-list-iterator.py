# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.arr = self.add_rec(nestedList, [])
        self.ci = 0

    def add_rec(self, arr, res):
        for i in arr:
            if i.isInteger():
                res.append(i.getInteger())
            else:
                res = self.add_rec(i.getList(), res)
        return res
        


    def next(self) -> int:
        ans = self.arr[self.ci]
        self.ci += 1
        return ans
            
    
    def hasNext(self) -> bool:
        return self.ci < len(self.arr)


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())