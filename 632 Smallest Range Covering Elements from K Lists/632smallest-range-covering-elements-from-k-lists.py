
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        
        heap = []

        cmax = float('-inf')

        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i][0], i, 0))
            cmax = max(cmax, nums[i][0])
        
        res = [float('-inf'), float('inf')]

        while heap:
            cmin, li, i = heapq.heappop(heap)
            if(cmax - cmin < res[1] - res[0]) or ((cmax - cmin == res[1] - res[0]) and cmin < res[0]):
                res = [cmin, cmax]
            if i + 1 < len(nums[li]):
                nxt = nums[li][i + 1]
                heapq.heappush(heap, (nxt, li, i + 1))
                cmax = max(cmax, nxt)
            else:
                break
        
        return res