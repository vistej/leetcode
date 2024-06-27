class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        a = edges[0]
        b = edges[1]
        if a[0] == b[0] or a[0] == b[1]:
            return a[0]
        elif a[1] == b[1] or a[1] == b[0]:
            return a[1]