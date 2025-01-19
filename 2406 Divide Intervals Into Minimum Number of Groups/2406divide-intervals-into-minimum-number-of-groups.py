import heapq

class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        r = []
        for b,e in intervals:
            if r and r[0] < b:
                heapq.heappop(r)
            heapq.heappush(r, e)
            

        
        return len(r)
