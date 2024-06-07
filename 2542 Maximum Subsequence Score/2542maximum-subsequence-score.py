class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        temp = []
        n = len(nums1)
        for i in range(n):
            temp.append((nums1[i], nums2[i]))
        
        temp.sort(key=lambda x: x[1])

        for i in range(n):
            nums1[i], nums2[i] = temp[i]
        
        h = []
        curr = ans = 0

        for i in range(n - 1, -1, -1):

            if len(h) > k - 1:
                curr -= heapq.heappop(h)
            
            heapq.heappush(h, nums1[i])
            curr += nums1[i]

            if len(h) == k:
                ans = max(ans, curr * nums2[i])
        
        return ans